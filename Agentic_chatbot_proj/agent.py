import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

# Load variables from .env
load_dotenv()

# Now it will work
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY= os.getenv("TAVILY_API_KEY")

groq_llm=ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


search_tool=TavilySearch(max_results=2)

system_prompt="Act as an AI chatbot who is smart and friendly"

agent=create_react_agent(
    model= groq_llm,
    tools=[search_tool],
    prompt=system_prompt
)
query="Tell me about the crypto trends and markets"


state={"message": query}

response= agent.invoke(state)

print(response)




