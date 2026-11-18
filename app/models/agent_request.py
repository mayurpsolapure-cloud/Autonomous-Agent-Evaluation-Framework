from pydantic import BaseModel,Field
from typing import Literal

ToolType = Literal["policy_tool", "ticket_tool", "email_tool"]
class AgentRequest(BaseModel):
    user_id:str=Field(min_length=3)
    session_id:str=Field(min_length=3)
    query:str=Field(min_length=5)
    simulate_failure: ToolType|None=None
