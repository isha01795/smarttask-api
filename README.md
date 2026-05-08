# SmartTask API 🚀

A secure backend task management system built with FastAPI, PostgreSQL, and JWT authentication.

---

## 🔥 Features

- User authentication (JWT)
- Secure password hashing (bcrypt)
- Create / Update / Delete tasks
- Task ownership protection
- Filtering + pagination
- RESTful API design
- Docker support

---

## ⚙️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)
- Docker

---

## 🚀 API Endpoints

### Auth
- POST /auth/signup
- POST /auth/login

### Tasks
- POST /tasks/
- GET /tasks/
- PATCH /tasks/{id}
- DELETE /tasks/{id}

---

## 🔐 Authentication

Use Bearer token:

Authorization:
Bearer <your_token>

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload