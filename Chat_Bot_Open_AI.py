import openai
import streamlit as st

openai.api_key = "sk-proj-9bfEsVVd8MN78dHejY3iT3BlbkFJxCc1xNDTli9inuDz39WR"
gptmodel = "text-davinci-003"
userrole = "user"

st.title('🤖💬 OpenAI Chatbot')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.empty():
        st.markdown(message["content"])

# User input
prompt = st.text_input("You:", "")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.empty():
        st.markdown(prompt)

    # Get response from OpenAI
    response = openai.Completion.create(
        engine=gptmodel,
        prompt="\n".join([msg["content"] for msg in st.session_state.messages]),
        max_tokens=150
    )

    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].text.strip()})
    with st.empty():
        st.markdown(response.choices[0].text.strip())
