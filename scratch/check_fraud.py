from backend.models.database import SessionLocal, ProctoringLog, InterviewSession
import json

db = SessionLocal()
try:
    logs = db.query(ProctoringLog).all()
    print(f"Total Proctoring Logs: {len(logs)}")
    for l in logs:
        print(f"Log: SessionID={l.session_id}, Event={l.event_type}, Confidence={l.confidence}")
    
    sessions = db.query(InterviewSession).all()
    for s in sessions:
        print(f"Session {s.session_id}: FraudScore={s.fraud_score}, Flags={s.fraud_flags}")
finally:
    db.close()
