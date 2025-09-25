from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from agent import get_response_agent
import uvicorn 

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


ALLOWED_MODELS=["llama-3.3-70b-versatile", "llama3-70b-8192"]


app= FastAPI(title="AI Agent")

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Agent")

# Allow frontend (React) to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODELS:
        return {"error": "Invalid Model Name"}
    
    llm_id=request.model_name
    query= request.messages
    allow_search=request.allow_search
    system_prompt= request.system_prompt
    provider= request.model_provider

    response= get_response_agent(llm_id, query,system_prompt, allow_search,provider)
    return response

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=9999)


