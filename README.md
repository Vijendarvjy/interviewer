# AI Interview System

An end-to-end AI interview platform built with FastAPI, SQLite, and vanilla HTML/CSS/JavaScript. Candidates can register, upload resumes, practice interviews, request scheduled interviews, answer AI-generated questions, and view reports. Admin users can manage sessions, schedule interview slots, review candidates, and download reports.

## Features

- Candidate registration and login with password reset support.
- Resume upload and extraction from PDF, DOCX, or TXT files.
- Practice interviews with a per-candidate attempt limit.
- Scheduled interviews that require both resume text and job description.
- AI-generated interview questions and AI-scored answers.
- Browser speech input/output support with backend speech endpoints.
- Proctoring event reporting and trust score tracking.
- Admin dashboard with Google-style light/dark theme.
- Admin session tools: search, filters, sorting, scheduling, CSV export, and report download.
- Admin candidate tools: search, filters, sorting, resume/JD review, CSV export.

## Tech Stack

- Backend: FastAPI, SQLAlchemy, Pydantic, Uvicorn.
- Database: SQLite by default.
- AI: OpenAI-compatible service with mock fallback.
- Documents: PyPDF2 and python-docx for resume parsing.
- Frontend: static HTML, CSS, and vanilla JavaScript modules.

## Run Locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables in `.env` as needed.

   The app can run without an AI key when `USE_MOCK_AI=true`.

3. Start the server:

   ```bash
   python run.py
   ```

4. Open the app:

   - Candidate UI: http://localhost:8000
   - Admin UI: http://localhost:8000/admin
   - Health check: http://localhost:8000/health

## Environment Variables

Common settings are read from `.env`:

```env
DEBUG=True
DATABASE_URL=sqlite:///./interview_system.db
OPENAI_API_KEY=
OPENAI_MODEL=gpt-3.5-turbo
USE_MOCK_AI=true
WHISPER_MODEL=base
SESSION_TIMEOUT_MINUTES=60
MAX_QUESTIONS_PER_SESSION=10
MAX_PRACTICE_SESSIONS_PER_CANDIDATE=2
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_TOKEN=local-admin-token
SMTP_HOST=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM=no-reply@localhost
```

## Project Structure

```text
backend/
  main.py                 FastAPI app, routers, static file mounting
  config.py               Environment-driven settings
  models/
    database.py           SQLAlchemy models and database setup
    schemas.py            Pydantic request/response models
  routers/
    admin.py              Admin auth, analytics, sessions, candidates
    interview.py          Candidate auth, scheduling, interview flow, reports
    proctoring.py         Proctoring event endpoints
    speech.py             Speech-to-text/text-to-speech endpoints
  services/
    ai_service.py         Question generation, scoring, report insights
    candidate_service.py  Candidate account/profile helpers
    datetime_utils.py     Datetime parsing helpers
    email_service.py      Password reset and schedule emails
    matching.py           Resume/JD/skill match scoring
    resume_service.py     Resume file parsing
    session_manager.py    In-memory active session state
    speech_service.py     Speech service integration

frontend/
  index.html              Candidate app shell
  admin.html              Admin app shell
  static/
    style.css             Candidate UI styles
    admin.css             Admin UI styles
    interview.js          Compatibility loader
    interview/app.js      Candidate app controller
    admin.js              Compatibility module entry
    admin/
      main.js             Admin bootstrap and global bindings
      state.js            Admin shared state/API headers
      utils.js            Admin shared formatting/CSV helpers
      layout.js           Theme, sidebar, navigation
      dashboard.js        Admin dashboard rendering
      sessions.js         Session list, filters, export, scheduling
      candidates.js       Candidate list, details, filters, export

run.py                    Development server entry point
requirements.txt          Python dependencies
interview_system.db       Local SQLite database
```

## Key Routes

- `GET /` - Candidate UI.
- `GET /admin` - Admin UI.
- `GET /health` - App health check.
- `POST /api/interview/register` - Register candidate.
- `POST /api/interview/login` - Candidate login.
- `POST /api/interview/upload-resume` - Extract resume text.
- `POST /api/interview/schedule` - Request scheduled interview.
- `GET /api/interview/room-status` - Check scheduled interview status.
- `POST /api/interview/start` - Start practice or scheduled interview.
- `POST /api/interview/answer/{session_id}/{question_id}` - Submit answer.
- `GET /api/interview/report/{session_id}` - Interview report data.
- `GET /api/interview/report/{session_id}/download` - Download text report.
- `POST /api/admin/login` - Admin login.
- `GET /api/admin/dashboard` - Admin metrics.
- `GET /api/admin/sessions` - Admin session list.
- `POST /api/admin/sessions/{session_id}/schedule-slot` - Schedule interview slot.
- `GET /api/admin/candidates` - Admin candidate list.

## Verification

Useful checks after changes:

```bash
python -m compileall backend
```

With the server running:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/admin
curl http://localhost:8000/static/admin/main.js
curl http://localhost:8000/static/interview/app.js
```

## Notes

- The admin CSS currently supports normal and dark themes.
- Admin JavaScript is modularized under `frontend/static/admin/`.
- The candidate app is loaded through `frontend/static/interview.js`, which delegates to `frontend/static/interview/app.js`.
- SQLite data is stored in `interview_system.db` unless `DATABASE_URL` is changed.
