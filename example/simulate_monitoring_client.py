import requests
import time

BASE_URL = "http://127.0.0.1:8000"

# create session
response = requests.post(
    f"{BASE_URL}/sessions",
    json={"candidate_name": "Demo Candidate"}
)

session_id = response.json()["session_id"]

print("Session Created:", session_id)

events = [
    "LOOKING_LEFT",
    "LOOKING_RIGHT",
    "PHONE_DETECTED",
    "ABNORMAL_MOVEMENT",
    "NO_FACE"
]

# send monitoring events
for event in events:

    r = requests.post(
        f"{BASE_URL}/monitoring/event",
        json={
            "session_id": session_id,
            "event_type": event
        }
    )

    print("Event Sent:", r.json())

    time.sleep(1)

# get final session result
final = requests.get(f"{BASE_URL}/sessions/{session_id}")

print("\nFinal Session State")
print(final.json())
