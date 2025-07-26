# Backend Service for Conversational AI

This project implements the backend service for a Conversational AI agent.

## Milestones Implemented
1. **Project Setup** – Directory structure and environment setup.
2. **Database Setup and Data Ingestion** – PostgreSQL configuration, schema creation, and CSV ingestion.
3. **Data Schemas** – Conversation history schema supporting multiple users and sessions.
4. **Core Chat API** – FastAPI-based REST endpoint `/api/chat`.
5. **LLM Integration and Business Logic** – Integrated Groq API (or mock) for conversational intelligence.

---

## **How to Run the Project**

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Setup PostgreSQL**
1. Install PostgreSQL (if not installed).
2. Create the database and user (update `.env` file with credentials).

### **3. Initialize Database**
```bash
python backend/database/init_db.py
```

### **4. Load Sample Data**
```bash
python backend/scripts/load_data.py
```

### **5. Run FastAPI Server**
```bash
uvicorn backend.main:app --reload
```

Then, visit `http://127.0.0.1:8000/docs` to test the API.

---

## **GitHub Submission**
- Commit after each milestone with messages like:
  ```
  feat: Complete Milestone 2 - Database Setup
  ```
- Final confirmation:
  ```
  I have completed all milestones and am ready to move forward.
  ```
