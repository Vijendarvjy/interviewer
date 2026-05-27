import sys
import os

# Append backend directory to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backend'))

from models.database import create_tables, engine
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "interview_system.db")
if os.path.exists(db_path):
    print(f"Deleting existing DB at {db_path}")
    try:
        os.remove(db_path)
        print("Deleted database file.")
    except Exception as e:
        print(f"Error deleting database: {e}")

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
