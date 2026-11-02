import queue
import threading


subscribers = {}
lock = threading.Lock()

# Sentinel event
DONE = {"type": "done"}


def subscribe(conversation_id):

    q = queue.Queue()

    with lock:

        if conversation_id not in subscribers:
            subscribers[conversation_id] = []

        subscribers[conversation_id].append(q)

    return q


def unsubscribe(conversation_id, q):

    with lock:

        if conversation_id in subscribers:

            if q in subscribers[conversation_id]:
                subscribers[conversation_id].remove(q)

            if not subscribers[conversation_id]:
                del subscribers[conversation_id]


def publish(conversation_id, event):

    with lock:

        queues = subscribers.get(conversation_id, []).copy()

    for q in queues:
        q.put(event)



