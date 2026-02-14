# 🤖 AI Chatbot - Streamlit Application

A production-ready, professional chatbot application built with Streamlit and powered by Google's Gemini AI.

## ✨ Features

- 💬 **Real-time Conversations**: Interactive chat interface with Google Gemini AI
- 📝 **Chat History**: Persistent storage of conversation history
- 💾 **Export Functionality**: Export chats to JSON or TXT format
- 🎨 **Modern UI**: Clean and responsive user interface
- ⚙️ **Configurable Settings**: Easy-to-modify configuration
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

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

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

### Starting a Conversation

1. Enter your Gemini API key in the sidebar (if not set in `.env`)
2. Type your message in the chat input at the bottom
3. Press Enter or click Send
4. View the AI's response in real-time

### Managing Chats

- **Clear Chat**: Click "Clear Chat History" in the sidebar
- **Save Chat**: Manually save with "Save Chat" button
- **Auto-save**: Enabled by default after each message

### Exporting Conversations

1. Click "JSON" or "TXT" in the Export section
2. Click the download button that appears
3. Save the file to your desired location

## 🔐 API Key Setup

### Option 1: Environment Variable (Recommended)

1. Copy `.env.example` to `.env`
2. Add your API key: `GEMINI_API_KEY=your_key_here`

### Option 2: Streamlit UI

1. Enter your API key in the sidebar input
2. The key will be stored for the current session

### Getting an API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy and save it securely

## 🛠️ Development

### Adding New Features

1. Create a new branch
2. Implement your feature
3. Test thoroughly
4. Submit a pull request

### Running Tests

```bash
# Add your test commands here
pytest tests/
```

## 📊 Features in Detail

### Chat Statistics

- Total message count
- User vs AI message breakdown
- Word count analytics
- Conversation metrics

### Export Formats

**JSON Export**
- Structured data format
- Includes timestamps
- Machine-readable
- Easy to parse

**TXT Export**
- Human-readable format
- Clean conversation layout
- Timestamped messages
- Easy to share

## 🚀 Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add `GEMINI_API_KEY` to secrets
5. Deploy!

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### Heroku

```bash
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues

**API Key Error**
- Verify your API key is correct
- Check if the API key has proper permissions
- Ensure it's properly set in `.env` or the UI

**Import Errors**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Activate your virtual environment

**Streamlit Won't Start**
- Check if port 8501 is available
- Try: `streamlit run app.py --server.port 8502`

**Chat History Not Saving**
- Check write permissions in the `data/` directory
- Ensure `AUTO_SAVE` is enabled in `config.py`

## 📧 Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Read the documentation

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Inspired by modern chat interfaces

## 📈 Roadmap

- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Custom themes
- [ ] Chat sharing functionality
- [ ] Advanced analytics dashboard
- [ ] Plugin system for extensions

---

**Made with ❤️ using Streamlit and Google Gemini AI**
