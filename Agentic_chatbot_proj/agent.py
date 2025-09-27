import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Load variables from .env
load_dotenv()

# Now it will work
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY= os.getenv("TAVILY_API_KEY")

# groq_llm=ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


# search_tool=TavilySearch(max_results=2)

# system_prompt="Act as an AI chatbot who is smart and friendly"


def get_response_agent(llm_id, query,system_prompt, allow_search,provider):
    if (provider=="Groq"):
        llm= ChatGroq(model=llm_id)

    tools=[TavilySearch(max_results=2)] if allow_search else []

    agent=create_react_agent(
        model= llm,
        tools=tools,
        prompt=system_prompt
    )
    # query="who is the previous prime minister of India"


    state = {
        "messages": [
            ("system", system_prompt),
            ("user", query)
        ]
    }

    response= agent.invoke(state)

    # print(response)

    messages= response.get("messages")


    ai_message= [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_message[-1]





