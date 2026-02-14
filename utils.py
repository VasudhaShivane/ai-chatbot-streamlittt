"""
Utility functions for the Streamlit Chatbot Application
"""

import streamlit as st
import json
from datetime import datetime
from pathlib import Path
from config import Config

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'api_key' not in st.session_state:
        st.session_state.api_key = Config.GEMINI_API_KEY
    
    if 'chat_id' not in st.session_state:
        st.session_state.chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")

def save_chat_history(messages, filename=None):
    """Save chat history to a JSON file"""
    try:
        if not filename:
            filename = f"chat_{st.session_state.chat_id}.json"
        
        filepath = Config.CHAT_HISTORY_DIR / filename
        
        chat_data = {
            'chat_id': st.session_state.chat_id,
            'timestamp': datetime.now().isoformat(),
            'messages': messages
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chat_data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        st.error(f"Error saving chat history: {str(e)}")
        return False

def load_chat_history(filename):
    """Load chat history from a JSON file"""
    try:
        filepath = Config.CHAT_HISTORY_DIR / filename
        
        with open(filepath, 'r', encoding='utf-8') as f:
            chat_data = json.load(f)
        
        return chat_data.get('messages', [])
    except Exception as e:
        st.error(f"Error loading chat history: {str(e)}")
        return []

def get_saved_chats():
    """Get list of saved chat files"""
    try:
        return sorted(
            Config.CHAT_HISTORY_DIR.glob('chat_*.json'),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
    except Exception as e:
        st.error(f"Error retrieving saved chats: {str(e)}")
        return []

def export_chat_to_json(messages):
    """Export chat history to JSON format"""
    chat_data = {
        'exported_at': datetime.now().isoformat(),
        'total_messages': len(messages),
        'messages': messages
    }
    return json.dumps(chat_data, indent=2, ensure_ascii=False)

def export_chat_to_txt(messages):
    """Export chat history to plain text format"""
    lines = [
        f"Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 60,
        ""
    ]
    
    for msg in messages:
        role = "You" if msg['role'] == 'user' else "AI Assistant"
        timestamp = msg.get('timestamp', '')
        content = msg['content']
        
        lines.append(f"[{timestamp}] {role}:")
        lines.append(content)
        lines.append("-" * 60)
        lines.append("")
    
    return "\n".join(lines)

def format_message_count(count):
    """Format message count for display"""
    if count == 0:
        return "No messages"
    elif count == 1:
        return "1 message"
    else:
        return f"{count} messages"

def truncate_text(text, max_length=100):
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def validate_api_key(api_key):
    """Validate the API key format"""
    if not api_key:
        return False, "API key is required"
    
    if len(api_key) < 20:
        return False, "API key seems too short"
    
    return True, "API key is valid"

def get_chat_statistics(messages):
    """Calculate chat statistics"""
    total_messages = len(messages)
    user_messages = sum(1 for msg in messages if msg['role'] == 'user')
    assistant_messages = total_messages - user_messages
    
    total_words = sum(len(msg['content'].split()) for msg in messages)
    
    return {
        'total_messages': total_messages,
        'user_messages': user_messages,
        'assistant_messages': assistant_messages,
        'total_words': total_words,
        'avg_words_per_message': total_words / total_messages if total_messages > 0 else 0
    }
