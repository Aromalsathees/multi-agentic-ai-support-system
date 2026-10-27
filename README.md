                                         🤖 AI Employees for Customer Support | Multi-Agent AI System

<p align="center">
  <strong>Introducing ARCHA — [ Autonomous Reasoning and Customer Help Assistant ] </strong>
</p><p align="center">
  An intelligent multi-agent AI system that automates customer support, evaluates potential fraud risks, retrieves company knowledge, and supports business decisions through collaborative AI agents.
</p></p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Claude%20API-Anthropic-D97757?style=for-the-badge" alt="Claude API"/>
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Database-orange?style=for-the-badge" alt="ChromaDB"/>
  <img src="https://img.shields.io/badge/SSE-Real--Time%20Streaming-0A7EA4?style=for-the-badge" alt="Server-Sent Events"/>
</p>

📸 Project Screenshots

<p align="center">
  <img width="100%" src="https://github.com/user-attachments/assets/0f4f4d06-c283-471a-bd1c-9d5f58d9280a" alt="ARCHA Customer Support Interface"/>
</p><p align="center">
  <img width="100%" src="https://github.com/user-attachments/assets/dceb3f6f-789e-409c-bd09-a58578ca9c1a" alt="ARCHA Admin Monitoring Dashboard"/>
</p>🚀 Overview

ARCHA (Autonomous Reasoning and Customer Help Assistant) is the primary AI employee in a multi-agent customer support system built with Python, Django, Claude API, Retrieval-Augmented Generation (RAG), and ChromaDB.

Unlike a traditional chatbot, ARCHA works with specialized AI agents to handle customer queries, retrieve relevant information, investigate potential fraud risks, and escalate complex cases for further evaluation.

The system also provides an admin monitoring dashboard to inspect conversations and observe AI agent activities in real time.

✨ Features

- 🤖 Multi-Agent AI Architecture
- 🔄 Autonomous Agent Collaboration
- 💬 Intelligent Customer Support Automation
- 📦 Order and Delivery Status Verification
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 ChromaDB Vector Database Integration
- 🔌 Claude API Integration
- 🛡️ Fraud Risk Assessment
- 💰 Refund and Compensation Decision Workflow
- 👨‍💼 Intelligent Issue Escalation
- ⚡ Real-Time Response and Activity Streaming
- 📊 Live Admin Monitoring Dashboard
- 🗂️ Conversation History and Agent Logs
- 🌐 Django-Powered Backend

🧠 AI Agents

1. ARCHA — Customer Support Agent

The primary AI employee responsible for customer interactions and support workflows.

- Understands and responds to customer queries.
- Retrieves order details and verifies delivery status.
- Checks refund history when required.
- Searches the company knowledge base for relevant information.
- Resolves common support requests using available tools.
- Escalates complex cases to the Manager Agent when necessary.

2. Manager Agent

Responsible for evaluating escalated customer issues and supporting business decisions.

- Reviews complex customer complaints.
- Evaluates refund and compensation requests.
- Considers available order information and relevant policies.
- Makes decisions or provides recommendations according to the configured workflow.

3. Risk Assessment Agent

Evaluates potentially suspicious customer, payment, and order scenarios.

- Identifies potential fraud indicators.
- Assesses risk using available information.
- Provides risk assessments and recommendations to the Manager Agent.
- Supports risk-aware decision-making.

📚 RAG Knowledge System

ARCHA uses Retrieval-Augmented Generation (RAG) with ChromaDB to retrieve relevant information from company policies, support documents, and business knowledge.

How It Works

Company Knowledge Documents
          ↓
     Text Chunking
          ↓
   Embedding Generation
          ↓
   ChromaDB Vector Store
          ↓
    Similarity Search
          ↓
   Relevant Context
          ↓
     LLM Response

Benefits

- Context-aware customer responses.
- Better alignment with company policies.
- Access to relevant business knowledge.
- Reduced reliance on the language model's internal knowledge alone.

RAG can reduce hallucinations but cannot eliminate them completely.

🔄 System Workflow

flowchart TD
    A[Customer Query] --> B[ARCHA Support Agent]
    B --> C{Required Action}
    C --> D[Order and Delivery Tools]
    C --> E[Refund History Tool]
    C --> F[RAG Knowledge Retrieval]
    C --> G[Risk Assessment Agent]
    G --> H[Manager Agent]
    D --> I[Support Workflow]
    E --> I
    F --> I
    H --> I
    I --> J[Customer Response]
    B --> K[Conversation and Agent Logs]
    K --> L[Live Admin Dashboard]

The execution path depends on the customer's query and the agent-routing logic.

📊 Admin Monitoring Dashboard

The dashboard provides visibility into customer conversations and agent execution.

- Monitor customer conversations.
- Inspect tool calls and tool results.
- Track agent activity and workflow execution.
- Review manager escalations and risk assessments.
- View conversation history and execution logs.
- Receive live updates through Server-Sent Events (SSE).

🛠️ Tech Stack

Category| Technologies
Programming Language| Python
Backend Framework| Django
AI Workflow Framework| LangChain
Language Model| Anthropic Claude API
Retrieval Architecture| RAG
Vector Database| ChromaDB
Database| PostgreSQL
Frontend| HTML, CSS, JavaScript
Frontend Rendering| Django Templates
Real-Time Communication| Server-Sent Events (SSE)
Version Control| Git, GitHub

🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Agentic AI application development.
- Multi-agent system architecture.
- LangChain and AI workflow orchestration.
- Tool calling and agent coordination.
- Retrieval-Augmented Generation.
- Embeddings and vector databases.
- LLM API integration.
- Django backend development.
- Real-time streaming with SSE.
- Conversation tracking and AI monitoring.

🔮 Future Improvements

- Persistent memory for AI agents.
- Multi-LLM provider support.
- Voice-based customer support.
- Advanced analytics and reporting.
- Human-in-the-loop approval workflows.
- Enhanced agent evaluation and monitoring.
- Improved failure recovery and automated testing.

👨‍💻 Author

Aromal Satheesh

Python Developer | Django Developer | Agentic AI Enthusiast

- 🌐 Portfolio: "arocode.vercel.app" (https://arocode.vercel.app)
- 💻 GitHub: "Aromalsatheesh" (https://github.com/Aromalsatheesh)

---

⭐ If you find this project interesting, consider giving the repository a star.
