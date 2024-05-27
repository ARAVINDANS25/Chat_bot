import openai
import streamlit as st

# Set OpenAI API key
with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key) == 51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

# Define function to interact with OpenAI API
def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response['choices'][0]['text'].strip()

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
