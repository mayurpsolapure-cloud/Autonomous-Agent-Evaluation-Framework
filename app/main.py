from fastapi import FastAPI
from app.models.agent_request import AgentRequest
from app.models.agent_response import AgentResponse,ToolCallResponse




app=FastAPI()

@app.get("/health")
def read_root():
    return {"status": "healthy"}

@app.post("/agent/run",response_model=AgentResponse)
def agent_post(request: AgentRequest):
    return{"user_id":request.user_id,"session_id":request.session_id,"query":request.query}    