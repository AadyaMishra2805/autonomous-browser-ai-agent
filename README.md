# Browser Agent AI

An autonomous AI-powered browser automation system that performs real-time intelligent web searches using browser control and workflow automation.

Built with:

- FastAPI
- Playwright
- Streamlit
- n8n
- ngrok

The project simulates a lightweight browser agent capable of searching the internet, scraping live results, and displaying them through a modern AI-style interface.

---

# ✨ Overview

This project combines browser automation with workflow orchestration to create a real-time AI search agent.

Instead of relying on APIs, the system opens a real browser using Playwright, performs searches dynamically, extracts search results, and returns them through an automated n8n pipeline.

The frontend is built with Streamlit and designed with a modern dark AI-agent style UI.

---

# 🚀 Core Features

- Real-time browser automation
- Live web searching with Playwright
- FastAPI backend service
- Workflow automation using n8n
- Public API exposure using ngrok
- Modern Streamlit interface
- Dynamic result extraction
- Search result cards with direct links
- AI-agent inspired UI

---

# 🧠 Architecture

```text
Streamlit Frontend
        ↓
     n8n Webhook
        ↓
    FastAPI Backend
        ↓
 Playwright Browser
        ↓
     Bing Search
        ↓
 Scraped Live Results
        ↓
Frontend Display
```

---

# 🛠️ Tech Stack

| Technology | Role |
|---|---|
| Python | Core Language |
| FastAPI | Backend API |
| Playwright | Browser Automation |
| Streamlit | Frontend UI |
| n8n | Workflow Automation |
| ngrok | Public Tunnel |

---

# 📁 Project Structure

```bash
browser-agent-ai/
│
├── app.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Guide

## 1. Clone Repository

```bash
git clone https://github.com/your-username/browser-agent-ai.git
```

```bash
cd browser-agent-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright

```bash
playwright install
```

---

# ▶️ Run Backend

```bash
uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# 🌐 Start ngrok

```bash
ngrok http 8000
```

Copy the generated public URL.

Example:

```text
https://your-ngrok-url.ngrok-free.app
```

---

# 🔄 n8n Workflow

Workflow:

```text
Webhook → HTTP Request → Respond to Webhook
```

---

## Webhook Node

| Setting | Value |
|---|---|
| Method | GET |
| Path | search-agent |

---

## HTTP Request Node

### URL

```text
https://your-ngrok-url.ngrok-free.app/search
```

### Query Parameter

| Name | Value |
|---|---|
| query | {{$json.query.query}} |

---

## Respond To Webhook Node

### Response Type

```text
JSON
```

### Response Body

```javascript
{{ JSON.stringify($json) }}
```

---

# 🎨 Run Frontend

```bash
streamlit run frontend.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# 🔍 Example Search

Example queries:

- laptop
- iphone
- AI tools
- gaming keyboard

---

# 📸 UI Preview

Add screenshots here.

---

# 🔮 Future Improvements

- Autonomous multi-step browsing
- AI summaries for search results
- Multi-search-engine support
- GPT integration
- Agent memory system
- Voice-based search
- Smart recommendation engine

---

# 👨‍💻 Developer

Aadya Mishra

---

# ⭐ Support

If you liked this project, consider giving it a star on GitHub.
