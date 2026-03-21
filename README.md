# Proctoring System Backend Integration

## Overview

This project implements the **backend integration module** for an **AI-Based Interview & Assessment System**.
It is responsible for receiving monitoring events from the candidate-side AI monitoring pipeline and calculating a **risk score for each candidate session**.

The backend receives signals such as suspicious movements or multiple people detection and updates the candidate’s **session risk status** in real time.

---

## Purpose

The monitoring system on the candidate side detects events like:

* PHONE_DETECTED
* MULTIPLE_PERSON_DETECTED
* NO_FACE
* LOOKING_LEFT
* LOOKING_RIGHT
* ABNORMAL_MOVEMENT

This backend service performs the following tasks:

* Receive monitoring events through API
* Process events through the monitoring bridge
* Calculate risk score using a rule-based risk engine
* Store candidate session status
* Provide APIs to view session details

---

## System Architecture

Monitoring Pipeline
↓
Backend API (FastAPI)
↓
Monitoring Bridge
↓
Risk Engine
↓
Session Store
↓
Admin Monitoring Service

---

## Project Structure

```
Proctoring-System-Backend-Integration/
│
├── app/
│   ├── api.py
│   └── schemas.py
│
├── services/
│   ├── monitoring_bridge.py
│   ├── risk_engine.py
│   └── session_store.py
│
├── examples/
│   └── simulate_monitoring_client.py
│
├── main.py
└── requirements.txt
```

---

## File Description

### main.py

Entry point of the application.
Starts the FastAPI server.

### app/api.py

Contains all API endpoints used to:

* create sessions
* receive monitoring events
* fetch session data

### app/schemas.py

Defines request models using **Pydantic** for data validation.

### services/monitoring_bridge.py

Handles communication between monitoring events and backend services.

### services/risk_engine.py

Implements rule-based risk scoring for violations.

### services/session_store.py

Maintains candidate session data in memory.

### examples/simulate_monitoring_client.py

A simulation script that mimics monitoring pipeline events for testing.

---

## Risk Engine Rules

| Violation                | Risk Score |
| ------------------------ | ---------- |
| PHONE_DETECTED           | +30        |
| MULTIPLE_PERSON_DETECTED | +50        |
| NO_FACE                  | +20        |
| LOOKING_LEFT             | +5         |
| LOOKING_RIGHT            | +5         |
| ABNORMAL_MOVEMENT        | +10        |

The risk score increases as more violations occur during the session.

---

## Installation

Clone the repository:

```
git clone https://github.com/jagruthi083/proctoring-system-backend-integration
```

Navigate to project folder:

```
cd Proctoring-System-Backend-Integration
```

Create virtual environment:

```
python -m venv .venv
```

Activate environment (Windows):

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Backend

Start the server:

```
python main.py
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## Testing the Monitoring System

Open a second terminal and run:

```
python examples/simulate_monitoring_client.py
```

This script will:

* Create a demo candidate session
* Send multiple monitoring violation events
* Update the risk score
* Display final session status

---

## API Endpoints

### Create Session

POST /sessions

### List Sessions

GET /sessions

### Get Session

GET /sessions/{session_id}

### Send Monitoring Event

POST /monitoring/event

---

## Example Event Request

```
POST /monitoring/event

{
  "session_id": "12345",
  "event_type": "PHONE_DETECTED"
}
```

---

## Expected Output

The system will:

* Receive violation events
* Update candidate risk score
* Track violations during session
* Store session state
* Allow admin services to view session data

Example session state:

```
{
  "candidate_name": "Demo Candidate",
  "risk_score": 65,
  "violations": [
    "LOOKING_LEFT",
    "PHONE_DETECTED",
    "NO_FACE"
  ]
}
```

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Requests

---

## Future Improvements

* Database integration (PostgreSQL / MongoDB)
* Real-time WebSocket dashboard
* Advanced AI-based risk analysis
* Admin monitoring interface
* Session recording storage

---

## Author

**Saurabh Ravindra Patil**

Task: Proctoring System Backend Integration

AI Based Interview & Assessment System
