# 🤖 AI Chatbot

A simple and elegant chatbot application powered by Google Gemini AI, built with Streamlit.

## ✨ Features

- 💬 Real-time AI conversations
- 📝 Auto-save chat history
- 💾 Export chats (JSON/TXT)
- 📊 Message statistics
- 🎨 Clean, modern interface

OUTPUTS:


![image_alt](https://github.com/VasudhaShivane/ai-chatbot-streamlittt/blob/2684189cb29a8886f6440daa4f8b45d97d592003/screenshots/Screenshot%202026-02-14%20144400.png)

![image_alt](https://github.com/VasudhaShivane/ai-chatbot-streamlittt/blob/9da33b77791f72fd0f3a976d6e1c4e306a302a31/screenshots/Screenshot%202026-02-14%20144504.png)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### 3. Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

## 📋 Requirements

- Python 3.8+
- Streamlit
- Google Generative AI
- Python-dotenv

## 🛠️ Configuration

Edit `config.py` to customize:
- AI model (default: `models/gemini-2.5-flash`)
- Chat history length
- UI theme
- Auto-save settings

## 📁 Project Structure

chatbot_streamlit_project/
├── app.py              # Main application
├── config.py           # Configuration settings
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
├── .env               # API key (create this)
└── data/              # Chat history storage




