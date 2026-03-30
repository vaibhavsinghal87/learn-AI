import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the question as best as you can."),
    ("user", "Quesion:{question}")
])

## Streamlit App
st.title("Ollama GenAI App")
input_text = st.text_input("Enter your question here:")

## Ollama LLM
llm=OllamaLLM(model="gemma3:1b")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
    try:    
        response=chain.invoke({"question": input_text})
        st.write(response)
    except Exception as e:
        st.error(f"Error: {str(e)}\n\nMake sure Ollama is running ('ollama serve') and model is installed ('ollama pull <model-name>')")