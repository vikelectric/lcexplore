import streamlit as st
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import prompts as pt
import initiate_connections as ic
import menu as mn
menu_string = mn.menu_summary_load()
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


# streamlit page configuration
st.set_page_config(
    page_title="Happy Meals",
    page_icon="🗺️",
    layout="centered"
)

# initialize the chat history as streamlit session state of not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit page title
st.title("🗺️ Happy Meals")
# streamlit page image
st.image(ic.working_dir + "/" + "Media" + "/" + "food_bgd.png", use_column_width = "auto")

system_prompt = [
        ("system",pt.system_prompt)
    ]

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message[0]):
        st.markdown(message[1])

# input field for user's message:
user_prompt = st.chat_input("Ask Bhojohori...")

if user_prompt:
    # display user entered message on screen
    st.chat_message("user").markdown(user_prompt)
    # add user entered message to chat history
    st.session_state.chat_history.append(("user", user_prompt))

    final_prompt = system_prompt + st.session_state.chat_history
    final_prompt_template = ChatPromptTemplate.from_messages(final_prompt)

    # Create the combined chain using LangChain Expression Language (LCEL)
    chat_output_chain = final_prompt_template | ic.llm | StrOutputParser()
    # Run the chain
    result = chat_output_chain.invoke({})
    st.session_state.chat_history.append(("assistant", result))

    # display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(result)