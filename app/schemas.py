from pydantic import BaseModel

# Request model to create session
class SessionCreate(BaseModel):
    candidate_name: str


# Monitoring event model
class MonitoringEvent(BaseModel):
    session_id: str
    event_type: str
