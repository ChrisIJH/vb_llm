"""
https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

streamlit run streamlit_chat_app_1.py  --server.port 8053
"""
import streamlit as st
import openai
from openai import OpenAI


st.title("Chat with me!")
st.write(openai.__version__)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])




if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = "gpt-3.5-turbo"



if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# with st.chat_message("user"):
#     st.write("Hello!")
# with st.chat_message("assistant"):
#     st.write("Hello!")
#     st.bar_chart({"A": 1, "B": 2, "C": 3})


# prompt = st.chat_input("Say something...", key="input_1")

if prompt:= st.chat_input("Say something..."):
    # st.write(f"User: {prompt}")
    # st.markdown(f"User: {prompt}")
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response block
    response = f"Echo: {prompt}"

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state['openai_model'],
            messages=[
                {"role": m['role'], "content": m['content']} 
                for m in st.session_state.messages
            ],
            stream = True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.write(st.session_state)