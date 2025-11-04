from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Language Translation App using Groq and LLama3"

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser=StrOutputParser()
##create chain
chain=prompt_template|model|parser

st.title("Language Translation app With Groq And LLama3")
user_input=st.text_input("Enter your text to translate")

if user_input:
    language_input=st.selectbox("Select Language to translate",["French","Hindi","Spanish","Oriya","English"])
    response = chain.invoke({'language':language_input,'text': user_input})
    st.success(response)
else:
    st.write("Please provide the text")