import streamlit as st
from chatbot_utils import get_answer

st.title("ForgeX💡")
st.caption(
    "Discover Scientific Insights: Get answers to your science questions from our knowledgeable chatbot."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hey there..!!"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"Echo: {prompt}"
    response = get_answer(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
