
# 📘 API Documentation – Secure Quiz Backend (Flask + MySQL)

This file documents all available backend API endpoints for the Secure & Cheating-Resistant Quiz Web Application.

---

## 👨‍🏫 Teacher Routes

### 🔐 POST `/teacher/login`
Login as teacher

**Body:**
```json
{
  "teacher_id": "T001",
  "full_name": "Manisha Kapila",
  "password": "1234"
}
```

**Response:**
```json
{ "success": true, "message": "Login successful", "teacher": { ... } }
```

---

### 📝 POST `/teacher/create-quiz`
Create a new quiz

**Body:**
```json
{
  "teacher_id": "T001",
  "title": "Python Basics"
}
```

---

### ➕ POST `/teacher/add-question`
Add question to a quiz

**Body:**
```json
{
  "quiz_id": 1,
  "question_text": "What is Python?",
  "option1": "Snake",
  "option2": "Programming language",
  "option3": "Game",
  "option4": "Car",
  "correct_option": 2
}
```

---

### 📊 GET `/teacher/results/<quiz_id>`
Get all student results of a quiz

---

## 👨‍🎓 Student Routes

### 🔐 POST `/student/login`
Login as student

**Body:**
```json
{
  "email": "test@gmail.com",
  "full_name": "Harsh Pareek",
  "course": "BCA"
}
```

---

### 📖 GET `/student/quiz/<quiz_id>`
Get all questions of a quiz (no correct answers sent)

---

### ✅ POST `/student/submit-response`
Submit selected option

**Body:**
```json
{
  "student_email": "test@gmail.com",
  "quiz_id": 1,
  "question_id": 2,
  "selected_option": 2
}
```

---

### 🚨 POST `/student/violation`
Log a cheating attempt

**Body:**
```json
{
  "student_email": "test@gmail.com",
  "quiz_id": 1,
  "reason": "Tab switch detected"
}
```

---

### 🧮 POST `/student/final-submit`
Submit the quiz & calculate result

**Body:**
```json
{
  "student_email": "test@gmail.com",
  "quiz_id": 1
}
```

---

### 📄 GET `/student/result/<quiz_id>/<student_email>`
Get final result

---

## ✅ Status Codes
- `200 OK` – Success
- `201 Created` – Data created
- `400 Bad Request` – Missing fields
- `401 Unauthorized` – Invalid credentials
- `404 Not Found` – Data not found
- `500 Internal Server Error` – Server/database issue

---

© 2025 Secure Quiz Team – Harsh Pareek (Backend Lead)
