# 🤖 Nexus Local LLM Interface

A professional and interactive web interface built with **Streamlit** to communicate with a locally installed Large Language Model (LLM) via **Ollama**.

## 🚀 Features
- **Local Inference:** 100% offline and secure, no data leaves your machine.
- **Streaming Responses:** Real-time text generation for a smooth user experience.
- **Chat History:** Maintains a sidebar log of the current session using Streamlit Session State.
- **Reset Functionality:** Easily clear the conversation and start fresh.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Ollama (Local API)
- **Model:** Llama 3.2 (or your preferred local model)
- **Language:** Python

## 📋 Prerequisites
Before running this project, ensure you have the following installed:
1. [Ollama](https://ollama.com/)
2. Python 3.8+

## ⚙️ Setup Instructions

1. **Install Ollama & Download Model:**
   Download Ollama and run the following command in your terminal:
   ```bash
   ollama run llama3.2
