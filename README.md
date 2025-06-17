# Job Success Compass 🎯

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://www.typescriptlang.org/)

A sophisticated web-based system that leverages machine learning to predict job application success probability. Built with Flask, TypeScript, and custom ML algorithms, it provides actionable insights to help users optimize their job search strategy.

![Project Demo](public/demo.png)

## 🌟 Features

- **Advanced ML Implementation**
  - Custom machine learning algorithms using NumPy
  - Real-time prediction updates
  - Interactive model training interface

- **User Management**
  - Secure authentication system
  - Role-based access control (Student/Admin)
  - Comprehensive profile management

- **Data Collection & Analysis**
  - Dynamic survey system
  - Interactive data visualization
  - Detailed success metrics

- **Modern UI/UX**
  - Responsive design
  - Dark/Light mode support
  - Accessible interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 16.x or higher
- npm/bun package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/job-success-compass.git
   cd job-success-compass
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Unix/MacOS
   source venv/bin/activate

   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   # or
   bun install
   ```

4. **Configure environment**
   Create a `.env` file with:
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

5. **Initialize database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Start development servers**
   ```bash
   # Terminal 1: Backend
   flask run

   # Terminal 2: Frontend
   npm run dev
   # or
   bun run dev
   ```

Visit `http://localhost:5000` to access the application.

## 🏗️ Project Structure

```
job-success-compass/
├── app/                    # Backend Flask application
│   ├── __init__.py        # App initialization
│   ├── models/            # Database models
│   ├── routes/            # API endpoints
│   ├── forms/             # Form validation
│   ├── templates/         # Jinja templates
│   ├── static/            # Static assets
│   └── ml/               # ML algorithms
├── src/                   # Frontend TypeScript/React
│   ├── components/        # UI components
│   ├── hooks/            # Custom React hooks
│   ├── pages/            # Page components
│   └── utils/            # Helper functions
├── migrations/            # Database migrations
├── instance/             # Instance configs
├── tests/                # Test suite
├── public/               # Public assets
└── config files          # Various config files
```

## 🧠 Machine Learning Model

Our system employs a sophisticated custom implementation of logistic regression for predicting job application success. The model considers various features:

| Feature | Description | Weight |
|---------|-------------|--------|
| Experience | Years in industry | High |
| Education | Degree level | Medium |
| Skills | Number of relevant skills | High |
| Industry | Target industry type | Medium |
| Job Changes | Previous transitions | Low |
| Certifications | Professional certs | Medium |
| Languages | Language proficiency | Low |
| Preparation | Interview readiness | High |

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/job-success-compass](https://github.com/yourusername/job-success-compass)

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [NumPy](https://numpy.org/)
- [React](https://reactjs.org/)
- All our contributors and supporters

## Project Overview

Job Success Compass is a web application designed to help job seekers improve their chances of success in job applications. It uses a machine learning model (logistic regression) to predict the probability of success based on various factors submitted by users through surveys. Employers can also post job offers, and job seekers can apply, receiving an instant success prediction.

The application includes:
- User authentication and roles (worker, employer, admin).
- A dashboard for users to view their survey results and public survey data.
- Functionality for job seekers to submit surveys about their experience, education, skills, etc.
- A machine learning model that predicts job application success probability.
- Job offer management for employers (create, edit, toggle active status, delete).
- A quick prediction feature for job offers without full application.

## Features

- **User Authentication:** Secure registration and login for job seekers and employers.
- **Role-Based Access:** Different functionalities based on user roles (worker, employer, admin).
- **Interactive Dashboard:** Personalized insights for job seekers, including success probability of their applications.
- **Survey Submission:** Users can submit detailed surveys about their professional background.
- **Machine Learning Predictions:**
    - Logistic Regression model for predicting job application success.
    - Provides a percentage chance of approval and identifies key influencing factors.
- **Job Offer Management:**
    - Employers can create, view, edit, and delete job offers.
    - Ability to activate/deactivate job offers.
- **Responsive UI:** Built with Flask and Tailwind CSS for a modern and responsive design.

## Setup and Installation

Follow these steps to get the Job Success Compass up and running on your local machine.

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git (optional, for cloning the repository)

### 1. Clone the Repository (Optional)

If you haven't already, clone the project repository:
```bash
git clone <repository_url>
cd 2425-11-b-pp-student-practices-assignment-SSPopov21
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is not present, you might need to create it manually or install packages individually: `pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Login Flask-Mail Flask-WTF python-dotenv scikit-learn numpy pandas joblib`)*

### 5. Initialize the Database

The application uses SQLite by default. Run the database migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application

```bash
flask run
```

The application should now be running on `http://127.0.0.1:5000`.

## Usage

- **Register:** Create a new user account (select 'worker' or 'employer' role).
- **Login:** Access your dashboard.
- **Worker (Job Seeker):**
    - Submit a new survey with your professional details.
    - View job offers and apply to get an instant success prediction.
    - Check your dashboard for survey results and success probabilities.
- **Employer:**
    - Publish new job offers.
    - Manage your existing job offers (edit, activate/deactivate, delete).
- **Admin:** (If you set `is_admin=True` for a user in the database)
    - Access the admin dashboard for user and survey management.

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** SQLite (SQLAlchemy ORM, Flask-Migrate)
- **Frontend:** HTML, Tailwind CSS, Jinja2 (templating)
- **Machine Learning:** Scikit-learn, NumPy (for logistic regression model)
- **User Management:** Flask-Login
- **Forms:** Flask-WTF

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
