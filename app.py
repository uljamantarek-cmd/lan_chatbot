import streamlit as st

from chatbot import get_response

st.set_page_config(page_title="LangChain Chatbot")
st.title("LangChain Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("Clear Chat"):
    st.session_state.history = []

for role, content in st.session_state.history:
    with st.chat_message(role):
        st.markdown(content)

user_input = st.chat_input("Ask a programming, math, or general question...")

if user_input:
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = get_response(user_input)

    with st.chat_message("assistant"):
        st.write(response["answer"])
        st.markdown(f"**Category:** {response['category']}")
        st.markdown(f"**Confidence:** {response['confidence']}")
        st.markdown(f"**Keywords:** {', '.join(response['keywords'])}")
        st.markdown(f"**Summary:** {response['summary']}")

    st.session_state.history.append(("assistant", response["answer"]))
