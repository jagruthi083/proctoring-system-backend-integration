from fastapi import APIRouter
from app.schemas import SessionCreate, MonitoringEvent
from services.session_store import create_session, get_sessions, get_session
from services.monitoring_bridge import process_event

router = APIRouter()

# Create a candidate session
@router.post("/sessions")
def create_session_api(session: SessionCreate):
    session_id = create_session(session.candidate_name)
    return {"session_id": session_id}


# List all sessions
@router.get("/sessions")
def list_sessions():
    return get_sessions()


# Get specific session
@router.get("/sessions/{session_id}")
def get_session_api(session_id: str):
    return get_session(session_id)


# Receive monitoring event
@router.post("/monitoring/event")
def monitoring_event(event: MonitoringEvent):
    return process_event(event.session_id, event.event_type)
