from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import initiate_connections as ic
def menu_summarize () :
    # read menu file
    file = open(ic.working_dir + "/" + "food_menu.xml", "r")
    menu = file.read()
    xml_to_summary_prompt = [
        ("system","you are a  program which condenses information into summaries without duplicates."
         "Please list out the menu information from the xml text submitted by the human "
         "and summarize the menu items in 300 words. Remove duplicates from your answer"),
        ("human","here is the menu I want summarized {menu1}")
    ]

    prompt_template_summary = ChatPromptTemplate.from_messages(xml_to_summary_prompt)

    # Create the combined chain using LangChain Expression Language (LCEL)
    chain = prompt_template_summary | ic.llm | StrOutputParser()

    # Run the chain
    result = chain.invoke({"menu1" : menu})
    return result

def menu_summary_load ():
    file = open(ic.working_dir + "/" + "italian_menu.txt", "r")
    menu_summary = file.read()
    return menu_summary

# messages = [
#     SystemMessage(content="answer the question asked "),
#     HumanMessage(content="create an italian restaurant menu of 50 items covering breakfast, lunch and dinner in xml format")
# ]
