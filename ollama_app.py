import streamlit as st
import requests
import json

st.set_page_config(page_title="Nexus Local AI", layout="wide")

st.title("🤖 Nexus Local LLM Interface")
st.subheader("Powered by Ollama | Secure & Offline")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.title("Settings")
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    st.write("### Recent Logs")
    for entry in st.session_state.chat_history:
        st.caption(f"{entry['role'].upper()}: {entry['content'][:25]}...")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

user_query = st.chat_input("Type your message here...")

if user_query:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        ui_update = st.empty()
        final_text = ""

        ollama_url = "http://localhost:11434/api/generate"
        config = {
            "model": "llama3.2",
            "prompt": user_query,
            "stream": True
        }

        try:
            req = requests.post(ollama_url, json=config, stream=True)
            for raw_data in req.iter_lines():
                if raw_data:
                    decoded_chunk = json.loads(raw_data.decode('utf-8'))
                    if 'response' in decoded_chunk:
                        content_piece = decoded_chunk['response']
                        final_text += content_piece
                        ui_update.markdown(final_text + "▒")

            ui_update.markdown(final_text)
            st.session_state.chat_history.append(
                {"role": "assistant", "content": final_text})

        except Exception as err:
            st.error(f"Connection failed: {err}")
