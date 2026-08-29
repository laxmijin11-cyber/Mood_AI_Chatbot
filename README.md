# 🤖 Mood Based AI Chatbot

A highly interactive, multi-personality AI chatbot built with **Streamlit** and **LangChain**. Switch between an **Angry**, **Funny**, or **Sad** AI agent and watch the conversation flow in real-time with persistent chat memory.

## ✨ Features

- **🎭 3 Unique AI Personalities**: Choose between Angry, Funny, and Sad modes to change the AI's tone and behavior.
- **🧠 Chat Memory**: Uses `st.session_state` to maintain the full conversation context (System, Human, and AI messages) across multiple user inputs.
- **💬 Real-Time Chat UI**: Built with Streamlit's modern `st.chat_input` and `st.chat_message` features for a professional, WhatsApp-like interface.
- **🔄 One-Click Reset**: Easily clear the conversation and start fresh with a single button.
- **🔒 Environment Security**: Loads API keys securely via `.env` files (using `python-dotenv`).

## 🛠️ Tech Stack

- **Frontend UI**: [Streamlit](https://streamlit.io/)
- **AI Framework**: [LangChain](https://www.langchain.com/)
- **Language Model**: [Mistral AI](https://mistral.ai/) (`mistral-small-2603`)
- **Environment Management**: `python-dotenv`

## 📋 Prerequisites

- Python 3.9+
- A [Mistral AI](https://console.mistral.ai/) API Key

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/laxmijin11-cyber/Mood_AI_Chatbot.git
   cd Mood_AI_Chatbot
