import streamlit as st
from langchain_openai import ChatOpenAI

st.title('Quickstart App')

# 1. Get the API key from the sidebar
# openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
openai_api_key = st.secrets['OPENAI_API_KEY']

def generate_response(input_text):
    # 2. Initialize the modern LangChain ChatOpenAI object
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=openai_api_key)
    
    # 3. Use .invoke() instead of calling the model like a function
    response = llm.invoke(input_text)
    
    # 4. Extract the content string from the response object
    st.info(response.content)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the capital of France?')
    submitted = st.form_submit_button('Submit')
    
    # Check if the user hasn't entered a valid-looking key yet
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)