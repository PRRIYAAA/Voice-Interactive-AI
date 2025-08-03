# Jarvis AI Agent

Jarvis is a real-time AI assistant built with Python using LiveKit and Gemini.  
It can listen, process, and respond intelligently with voice.

---

## Features
- Real-time audio interaction via LiveKit
- AI-powered responses using Gemini
- Easy to extend for custom behaviors

---

## Requirements
- Python 3.9 or higher
- LiveKit Server running locally or remotely
- LiveKit API credentials (API Key, API Secret)
- Gemini model enabled through LiveKit Plugins
---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/jarvis-ai.git
   cd jarvis-ai
   
   
2. Create and activate a virtual environment
  ``` 
   python -m venv venv
   source venv/bin/activate   
   Windows: venv\Scripts\activate
   
   
3. Configuration
   ```
   Create a .env file in the project root:
   
   LIVEKIT_URL=ws://localhost:7880
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret

4.Generate Requirements
   ```
   If you add new libraries, update requirements.txt:
   pip freeze > requirements.txt

5.Run the Agent
```
   python agent.py


## Project Structure
```
├── agent.py # Main AI agent logic
├── prompt.py # Agent instructions and response templates
├── requirements.txt # Python dependencies
├── .env # Environment variables (not uploaded to GitHub)
├── .gitignore # Files and folders ignored by Git
└── README.md # Project documentation



