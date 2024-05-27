import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "sk-proj-9bfEsVVd8MN78dHejY3iT3BlbkFJxCc1xNDTli9inuDz39WR"

# Define function to interact with OpenAI API
def get_chat_response(messages):
    response = openai.Completion.create(
        engine="davinci",
        prompt=messages,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

# Streamlit app
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
    response = get_chat_response("\n".join([msg["content"] for msg in st.session_state.messages]))

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.empty():
        st.markdown(response)
