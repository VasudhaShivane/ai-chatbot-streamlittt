
import streamlit as st
import google.generativeai as genai
from datetime import datetime
import json
import os
from pathlib import Path
from config import Config
from utils import (
    initialize_session_state,
    save_chat_history,
    load_chat_history,
    export_chat_to_json,
    export_chat_to_txt
)

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

def configure_genai():
    """Configure the Gemini AI model"""
    api_key = st.session_state.get('api_key') or Config.GEMINI_API_KEY
    if not api_key:
        st.error("⚠️ API Key not found! Please enter your Gemini API key in the sidebar.")
        st.stop()
    
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel(Config.MODEL_NAME)
    except Exception as e:
        st.error(f"Error configuring AI model: {str(e)}")
        st.stop()

def display_chat_history():
    """Display the chat history with styled messages"""
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        timestamp = message.get("timestamp", "")
        
        if role == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(f"**You** - *{timestamp}*")
                st.markdown(content)
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(f"**AI Assistant** - *{timestamp}*")
                st.markdown(content)

def get_ai_response(model, prompt):
    """Get response from Gemini AI"""
    try:
        # Add conversation history for context
        conversation_context = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
            for msg in st.session_state.messages[-Config.MAX_HISTORY:]
        ])
        
        full_prompt = f"{conversation_context}\nUser: {prompt}\nAssistant:"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.title("CHATBOT")
        
        
        
        st.divider()
        
        # Chat controls
        st.subheader("💬 Chat Controls")
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        if st.button("💾 Save Chat", use_container_width=True):
            if st.session_state.messages:
                save_chat_history(st.session_state.messages)
                st.success("Chat saved successfully!")
            else:
                st.warning("No messages to save!")
        
        st.divider()
        
        # Export options
        st.subheader("📤 Export Chat")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("JSON", use_container_width=True):
                if st.session_state.messages:
                    json_data = export_chat_to_json(st.session_state.messages)
                    st.download_button(
                        label="Download JSON",
                        data=json_data,
                        file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
        
        with col2:
            if st.button("TXT", use_container_width=True):
                if st.session_state.messages:
                    txt_data = export_chat_to_txt(st.session_state.messages)
                    st.download_button(
                        label="Download TXT",
                        data=txt_data,
                        file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
        
        st.divider()
        
        # Statistics
        st.subheader("📊 Statistics")
        st.metric("Total Messages", len(st.session_state.messages))
        user_msgs = sum(1 for msg in st.session_state.messages if msg["role"] == "user")
        st.metric("Your Messages", user_msgs)
        st.metric("AI Responses", len(st.session_state.messages) - user_msgs)
        
        st.divider()
        
        # About section
        st.subheader("ℹ️ About")
        st.info("""
        **AI Chatbot v1.0**
        
        Powered by Google Gemini AI
        
        Features:
        - Real-time conversations
        - Chat history
        - Export conversations
        - Persistent storage
        """)
    
    # Main content area
    st.markdown('<h1 class="main-header">🤖 AI Chatbot Assistant</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Configure AI model
    model = configure_genai()
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Add user message to chat
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": timestamp
        })
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.markdown(f"**You** - *{timestamp}*")
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                response = get_ai_response(model, prompt)
                response_timestamp = datetime.now().strftime("%H:%M:%S")
                st.markdown(f"**AI Assistant** - *{response_timestamp}*")
                st.markdown(response)
        
        # Add assistant message to chat
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": response_timestamp
        })
        
        # Auto-save after each interaction
        if Config.AUTO_SAVE:
            save_chat_history(st.session_state.messages)

if __name__ == "__main__":
    main()
