from services.risk_engine import calculate_risk
from services.session_store import update_session

# Process monitoring events from AI pipeline
def process_event(session_id, event_type):

    # calculate risk score
    risk = calculate_risk(event_type)

    # update session information
    update_session(session_id, event_type, risk)

    return {
        "session_id": session_id,
        "event": event_type,
        "risk_added": risk
    }
