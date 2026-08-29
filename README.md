# 🤖 Mood Based AI Chatbot

A multi-personality AI chatbot built with **Streamlit** and **LangChain**, powered by **Mistral AI**. 
Users can switch between **Angry**, **Funny**, and **Sad** personalities to experience completely different conversational styles.

---

## 📸 Project Preview

<img width="596" height="264" alt="image" src="https://github.com/user-attachments/assets/f8fe3861-867b-48c1-a3bb-af21518fc1ff" />



---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🎭 **3 Personas** | Switch between Angry, Funny, and Sad AI personalities instantly. |
| 🧠 **Chat Memory** | Uses `st.session_state` to retain the full conversation context. |
| 💬 **Modern UI** | Built with `st.chat_input` and `st.chat_message` for a clean, chat-like interface. |
| 🔄 **Reset Chat** | One-click button to clear the conversation and start fresh. |
| 🔒 **Security** | Loads API keys securely using `python-dotenv`. |

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| Frontend UI | Streamlit |
| AI Framework | LangChain |
| Language Model | Mistral AI (`mistral-small-2603`) |
| Environment | Python 3.9+ |

---

## 📁 Project Structure

```text
Mood_AI_Chatbot/
├── UIchatbot.py                 # Main Streamlit application
├── requirements.txt       # List of Python dependencies
├── .env                   # API keys (DO NOT push to GitHub)
└── README.md              # Project documentation
