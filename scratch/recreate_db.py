from backend.models.database import create_tables, engine, Base
import os

# Ensure the DB file is gone
db_path = "ai_interview.db"
if os.path.exists(db_path):
    print(f"Deleting existing DB at {db_path}")
    os.remove(db_path)

print("Creating tables...")
create_tables()
print("Tables created successfully.")

# Verify columns
from sqlalchemy import inspect
inspector = inspect(engine)
columns = [c['name'] for c in inspector.get_columns('interview_sessions')]
print(f"Columns in interview_sessions: {columns}")
if 'fraud_score' in columns:
    print("SUCCESS: fraud_score column found!")
else:
    print("FAILURE: fraud_score column missing!")
