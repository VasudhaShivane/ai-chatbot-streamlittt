# 🤖 AI Chatbot - Streamlit Application


## ✨ Features

- 💬 **Real-time Conversations**: Interactive chat interface with Google Gemini AI
- 📝 **Chat History**: Persistent storage of conversation history
- 💾 **Export Functionality**: Export chats to JSON or TXT format
- 🎨 **Modern UI**: Clean and responsive user interface
- 📊 **Chat Statistics**: Track message counts and conversation metrics
- 🔒 **Secure**: API key management with environment variables

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chatbot_streamlit_project
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your API key
   # GEMINI_API_KEY=your_actual_api_key_here
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
chatbot_streamlit_project/
├── app.py                  # Main Streamlit application
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── data/                 # Data directory (created automatically)
    └── chat_history/     # Saved chat histories
```

## 🔧 Configuration

Edit `config.py` to customize:

- **Model Settings**: Change AI model, temperature, etc.
- **UI Theme**: Modify colors and styling
- **Chat Settings**: Adjust history length, auto-save behavior
- **Safety Settings**: Configure content filtering

## 📖 Usage Guide

### Managing Chats

- **Clear Chat**: Click "Clear Chat History" in the sidebar
- **Save Chat**: Manually save with "Save Chat" button
- **Auto-save**: Enabled by default after each message

### Exporting Conversations

1. Click "JSON" or "TXT" in the Export section
2. Click the download button that appears
3. Save the file to your desired location

## 🔐 API Key Setup

### Environment Variable 

1. Copy `.env.example` to `.env`
2. Add your API key: `GEMINI_API_KEY=your_key_here`


### Getting an API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and save it securely

## 📊 Features in Detail

### Chat Statistics

- Total message count
- User vs AI message breakdown
- Word count analytics
- Conversation metrics

### Export Formats

**JSON Export**
**TXT Export**



**Made with ❤️ using Streamlit and Google Gemini AI**
