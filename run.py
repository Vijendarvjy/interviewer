import uvicorn
import os
import sys

# Ensure backend is in path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

if __name__ == "__main__":
    print("Starting AI Interview System...")
    print("Access the Student UI at: http://localhost:8000")
    print("Access the Admin Dashboard at: http://localhost:8000/admin")
    
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
