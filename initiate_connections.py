from langchain_groq import ChatGroq
import os
#import json
import streamlit as st

# get working directory of the actual strteamlit environment
working_dir = os.path.dirname(os.path.abspath(__file__))

'''
#read the config file for API Key(s)
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]
'''

#read the config file for API Key(s) --- STREAMLIT Version
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]



# save the api key to environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(
    # model="llama-3.1-8b-instant",
    model="llama-3.1-70b-versatile",
    temperature=0.0,
    max_retries=2,
    # other params...
)
