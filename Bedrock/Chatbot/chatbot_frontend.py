# streamlit_chat.py
import streamlit as st
import chatbot_backend as demo   # your backend module

st.set_page_config(page_title="Chatbot Anisha", page_icon="🤖")
st.title("Hi, This is Chatbot 😎")

# --- initialize LLM and history in session state ---
if "llm" not in st.session_state:
    # change profile/model_id if you need to
    st.session_state.llm = demo.get_llm(profile="default", model_id="amazon.titan-text-lite-v1")

if "history" not in st.session_state:
    # SimpleHistory(max_turns=6) keeps recent turns
    st.session_state.history = demo.SimpleHistory(max_turns=6)

# optional system instruction that demo.demo_converse will try to apply
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful assistant. Keep answers concise."

# --- render previous chat from history ---
# history.messages is a list of {"role": "user"/"assistant", "text": "..."}
for msg in st.session_state.history.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# --- input box ---
user_input = st.chat_input("Chat with Chatbot — ask anything...")

if user_input:
    # show user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # call backend: demo_converse(user_text, llm, history, system_prompt)
    try:
        assistant_reply = demo.demo_converse(
            user_text=user_input,
            llm=st.session_state.llm,
            history=st.session_state.history,
            system_prompt=st.session_state.system_prompt
        )
    except Exception as e:
        assistant_reply = f"Error calling the model: {e}"

    # show assistant message and it will also be saved into history inside demo_converse
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

# --- optional controls ---
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("Clear chat"):
        st.session_state.history = demo.SimpleHistory(max_turns=6)
        # force rerun to clear UI
        st.experimental_rerun()

with col2:
    st.caption("Model: " + getattr(st.session_state.llm, "model", "unknown"))
