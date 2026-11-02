from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, StreamingHttpResponse
from django.contrib.admin.views.decorators import staff_member_required

import json

from .langchain_agents import run_support_agent
from .event_queue import publish, subscribe, unsubscribe
from .models import Conversation, Message
from orders.models import Order


def extract_response_text(response):
    """Convert Claude/LangChain response into plain text."""

    if isinstance(response, str):
        return response

    if isinstance(response, list):
        return "\n".join(
            extract_response_text(item)
            for item in response
            if item is not None
        )

    if isinstance(response, dict):
        if response.get("type") == "text":
            return response.get("text", "")

        if "content" in response:
            return extract_response_text(response["content"])

        if "text" in response:
            return extract_response_text(response["text"])

        return json.dumps(response, default=str)

    if hasattr(response, "content"):
        return extract_response_text(response.content)

    return str(response)


def chat(request, order_id):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=405)

    data = json.loads(request.body)
    user_message = data.get("message")

    if not user_message:
        return JsonResponse({"error": "Empty message"}, status=400)

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    conversation, created = Conversation.objects.get_or_create(
        user=request.user,
        order=order
    )

    # Save customer message
    Message.objects.create(
        conversation=conversation,
        role="user",
        content=user_message
    )

    # Publish customer message to dashboard
    publish(conversation.id, {
        "type": "user_message",
        "message": user_message,
        "name": request.user.first_name
    })

    try:

        # Run multi-agent support system
        raw_reply = run_support_agent(
            user_message,
            conversation.id,
            order.id,
            request.user.id
        )

        # Convert response into plain text
        reply = extract_response_text(raw_reply)

        # Save AI response
        Message.objects.create(
            conversation=conversation,
            role="assistant",
            content=reply
        )

        # Publish final response to dashboard
        publish(conversation.id, {
            "type": "final",
            "message": reply
        })

        return JsonResponse({"reply": reply})

    finally:

        # Tell dashboard that processing is completed
        publish(conversation.id, {
            "type": "done"
        })


@staff_member_required
def dashboard(request):

    conversations = Conversation.objects.all().order_by("-created_at")

    context = {
        "conversations": conversations,
    }

    return render(request, "dashboard/dashboard.html", context)


@staff_member_required
def conversation_detail(request, conversation_id):

    conversation = get_object_or_404(
        Conversation,
        id=conversation_id
    )

    messages = conversation.messages.order_by("created_at")
    agentlogs = conversation.agentlogs.order_by("created_at")

    context = {
        "conversation": conversation,
        "messages": messages,
        "agentlogs": agentlogs
    }

    return render(
        request,
        "dashboard/conversation_detail.html",
        context
    )


@staff_member_required
def conversation_stream(request, conversation_id):

    # Verify conversation exists
    get_object_or_404(Conversation, id=conversation_id)

    def event_stream():

        q = subscribe(conversation_id)

        try:

            while True:

                try:
                    event = q.get(timeout=15)

                    yield f"data: {json.dumps(event, default=str)}\n\n"

                except __import__("queue").Empty:

                    # Keep SSE connection alive
                    yield ": keep-alive\n\n"

        finally:

            unsubscribe(conversation_id, q)


    response = StreamingHttpResponse(
        event_stream(),
        content_type="text/event-stream"
    )

    response["Cache-Control"] = "no-cache"
    response["X-Accel-Buffering"] = "no"

    return response