# Risk scoring rules

RISK_RULES = {
    "PHONE_DETECTED": 30,
    "MULTIPLE_PERSON_DETECTED": 50,
    "NO_FACE": 20,
    "LOOKING_LEFT": 5,
    "LOOKING_RIGHT": 5,
    "ABNORMAL_MOVEMENT": 10
}

def calculate_risk(event_type):
    return RISK_RULES.get(event_type, 1)
