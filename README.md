# Disease-Prediction-Using-Python
Disease Prediction System using Machine Learning and Python
# Disease Prediction System

An AI-powered medical assistant chatbot built with Python, Flet, and Ollama (local LLM). The system answers health and symptom-related questions only, using a locally-run AI model — no internet/cloud API required.

## Features
- Chat-based interface built with Flet
- Local AI inference using Ollama (Llama 3.2)
- Restricted to medical/health topics only (keyword-based filtering + system prompt)
- Non-blocking UI (background threading for AI responses)
- Fully offline after setup — no external API keys needed

## Tech Stack
- **Python 3.12**
- **Flet** — UI framework
- **Ollama** — local LLM runtime
- **Llama 3.2** — language model (via Ollama)

## Project Structure
disease_prediciton_system/
│
├── main.py              # UI and app entry point
├── chatbot.py            # Chat logic and medical topic filtering
├── model.py               # Connects to local Ollama model
├── requirements.txt
├── README.md
│
├── assets/                # Images/icons (logo, avatars, etc.)
├── screenshots/          # App screenshots
└── docs/                   # Project report, PPT,
Documentation
## Setup Instructions

### 1. Install Ollama
Download and install from [ollama.com](https://ollama.com)

### 2. Pull the AI model
ollama pull llama3.2
### 3. Install Python dependencies
pip install -r requirements.txt
### 4. Run the application
python main.py
## How It Works
1. User types a message describing symptoms or a health question
2. `chatbot.py` checks if the message is medical-related using keyword matching
3. If medical, the message is sent to `model.py`, which calls the local Llama 3.2 model via Ollama, using a system prompt that restricts responses to health topics
4. If non-medical, the system responds with a polite refusal instead of calling the AI
5. The response is displayed in the chat window (runs in a background thread so the UI stays responsive)

## Limitations
- Keyword-based filtering can be bypassed by phrasing or typos (not NLP-based intent detection)
- No conversation memory yet — each message is treated independently
- Requires Ollama installed locally; not usable without it

## Future Improvements
- Add conversation memory for multi-turn symptom discussions
- NLP-based intent classification instead of keyword matching
- Polished UI with chat bubbles, avatars, and branding
- Disease prediction based on structured symptom input (dataset-driven)

## Author
[Aadhar shukla] — CSVTU Vocational training Project, [2026]