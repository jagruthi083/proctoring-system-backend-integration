import uuid

# in-memory session storage
sessions = {}

# create new session
def create_session(candidate_name):

    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "candidate_name": candidate_name,
        "risk_score": 0,
        "violations": []
    }

    return session_id


# get all sessions
def get_sessions():
    return sessions


# get single session
def get_session(session_id):
    return sessions.get(session_id)


# update session risk and violations
def update_session(session_id, event_type, risk):

    if session_id in sessions:

        sessions[session_id]["violations"].append(event_type)

        sessions[session_id]["risk_score"] += risk
