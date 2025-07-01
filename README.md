# 🎓 Quiz Master – A Full-Stack Exam Preparation Platform

**Quiz Master** is a multi-user web application built as part of the **Modern Application Development 2 (MAD2)** capstone project at **IIT Madras**. The platform enables seamless quiz management and participation for various academic subjects, supporting roles for both admins and users.

## 🚀 Project Overview

**Quiz Master** acts as an interactive exam preparation site, supporting two roles:

- **Admin (Quiz Master)** – Manages users, subjects, chapters, quizzes, and questions  
- **User** – Can register, log in, attempt quizzes, and view scores

The system was built for scalability, security, and ease of use, with modern UI/UX and optimized backend logic.

---

## 🛠️ Tech Stack

- **Frontend**: Vue.js with Vue CLI  
- **Backend**: Flask (RESTful API)  
- **Database**: SQLite  
- **ORM**: SQLAlchemy  
- **Caching**: Redis  
- **Background Jobs**: Celery with Redis  

---

## 🧩 System Design & Features

- **User Authentication** using JWT tokens (login, registration, token refresh)  
- **Admin Dashboard** for managing:
  - Users, Subjects, Chapters
  - Quiz creation, editing, and deletion
  - Quiz data export (CSV)
  - Performance monitoring
- **User Features**:
  - Register and log in securely
  - Browse available quizzes
  - Attempt quizzes with MCQs
  - View past scores and progress

---

## 🗃️ Database Model (ER Diagram Highlights)

- **User Table**: Stores credentials, personal details, and scores  
- **Subject Table**: Subjects created by admins  
- **Chapter Table**: Chapters under each subject  
- **Quiz Table**: Metadata of quizzes (date, duration, chapter)  
- **Question Table**: MCQs with options and answers  
- **Scores Table**: Tracks user attempts and performance

---

## 🔌 API Endpoints

### 🔐 Authentication
- `POST /login` – User login  
- `POST /register` – New user registration  
- `POST /refresh` – Refresh JWT access token  

### 👥 Users
- `GET /users` – List all users (admin only)  
- `POST /users` – Create new user  
- `GET /users/<user_id>` – Get user details  
- `PUT /users/<user_id>` – Update user info  
- `DELETE /users/<user_id>` – Delete user  

### 📚 Subjects & Chapters
- `GET /subjects`, `POST /subjects` – Manage subjects  
- `PUT/DELETE /subjects/<subject_id>`  
- `GET /chapters`, `POST /chapters` – Manage chapters  
- `PUT/DELETE /chapters/<chapter_id>`

### 📝 Quizzes & Questions
- `GET /quizzes`, `POST /quizzes` – Create & view quizzes  
- `PUT/DELETE /quizzes/<quiz_id>`  
- `GET /quiz/<chapter_id>` – Quizzes by chapter  
- `GET /QuizQues/<quiz_id>` – Fetch quiz questions  

### 🧮 Scores & Analytics
- `POST /scores` – Submit quiz score  
- `GET /scores/<user_id>` – View user scores  
- `GET /adminscores` – View all user scores (admin)  
- `GET /adminscores/<user_id>` – View specific user scores  
- `GET /summary` – Admin summary report  
- `GET /avgmarks` – View average marks

---

## ✅ Outcome

- Successfully developed and deployed all core functionalities  
- Provides a user-friendly platform for quiz preparation and result tracking  
- Robust admin tools for quiz and user management  
- Scalable architecture with Redis and Celery for async job handling  

---

## 📌 Future Enhancements

- Add support for timed quizzes with automatic submission  
- Integrate email notifications for quiz reminders  
- Support quiz tagging by difficulty level  
- Add leaderboard and gamification features

---


## 📎 License

This project was built as an academic submission and is intended for educational use only.

---

