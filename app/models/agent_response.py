from pydantic import BaseModel,Field
from typing import Literal,Any

status_codes=Literal[
    "success",
    "failed",
    "needs_clarification",
    "unsupported"
]
class ToolCallResponse(BaseModel):
    tool_name:str
    parameters:dict[str,Any]
    status:str
    result:dict[str,Any]|None=None
    error:str|None=None
class AgentResponse(BaseModel):
    status:status_codes
    final_response:str
    plan:list[str]
    tool_calls:list[ToolCallResponse]
    errors:list[str]
    latency_ms:float

    