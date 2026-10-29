
import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "qwen2.5:3b"

st.set_page_config(
    page_title="BOARD-AI",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ BOARD-AI")
st.caption("Offline AI Assistant for Technical Board Analysis")

st.sidebar.header("System Status")

try:
    r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
    r.raise_for_status()
    st.sidebar.success("Ollama Connected")
    st.sidebar.write(f"Model: {MODEL_NAME}")
except requests.RequestException:
    st.sidebar.error("Ollama Not Connected")

st.header("Engineering Assistant")

uploaded_files = st.file_uploader(
    "Upload Engineering Documents",
    type=["pdf", "txt", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")
    for file in uploaded_files:
        st.write(f"📄 {file.name}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your engineering question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("BOARD-AI is thinking..."):
            try:
                response = requests.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": MODEL_NAME,
                        "prompt": question,
                        "stream": False
                    },
                    timeout=300
                )
                response.raise_for_status()
                answer = response.json()["response"]
            except requests.RequestException as error:
                answer = f"Error communicating with Ollama: {error}"

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
