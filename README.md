# Job Success Compass 🎯

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://www.typescriptlang.org/)

A modern web application that leverages machine learning to predict job application success. Built with Flask, TypeScript, and custom ML algorithms, it empowers job seekers and employers with actionable insights and a seamless experience.

![Project Demo](public/demo.png)

---

## 🚀 Features

- **ML-Powered Predictions:** Real-time job application success probability using custom logistic regression (NumPy).
- **User Roles:** Secure authentication for job seekers, employers, and admins.
- **Survey System:** Collects and analyzes user data for better predictions.
- **Job Offer Management:** Employers can post, edit, and manage job offers.
- **Interactive Dashboard:** Personalized analytics and visualizations.
- **Modern UI/UX:** Responsive, accessible, and supports dark/light mode.

---

## 🏁 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or bun

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd 2425-11-b-pp-student-practices-assignment-SSPopov21
   ```
2. **Set up Python environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Install frontend dependencies**
   ```bash
   npm install
   # or
   bun install
   ```
4. **Configure environment**
   Create a `.env` file in the root with:
   ```env
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///job_success.db
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   ```
5. **Initialize the database**
   ```bash
   flask db upgrade
   ```
6. **Run the app**
   - Backend: `flask run`
   - Frontend: `npm run dev` or `bun run dev`

Visit [http://localhost:5000](http://localhost:5000) for the backend and [http://localhost:5173](http://localhost:5173) for the frontend (if using Vite).

---

## 🗂️ Project Structure

```
2425-11-b-pp-student-practices-assignment-SSPopov21/
├── app/           # Flask backend (models, routes, ML, forms, templates)
├── src/           # React/TypeScript frontend (components, pages, utils)
├── migrations/    # Database migrations
├── public/        # Public assets (images, favicon, etc.)
├── requirements.txt
├── run.py         # Flask entry point
└── ...            # Configs, docs, etc.
```

---

## 🧠 Machine Learning Model

- **Algorithm:** Custom logistic regression (NumPy)
- **Features:** Experience, education, skills, industry, job changes, certifications, languages, interview preparation
- **Output:** Success probability and key influencing factors

---

## 🛠️ Technologies Used
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF, NumPy
- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Database:** SQLite (default, via SQLAlchemy)
- **Other:** Python-dotenv, WTForms

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes
4. Push and open a Pull Request

---

## 📬 Contact

Author: Your Name  
Email: email@example.com  
Project Link: [https://github.com/yourusername/job-success-compass](https://github.com/yourusername/job-success-compass)

---

## 🙏 Acknowledgments
- Flask, TypeScript, NumPy, React, and all contributors

---
