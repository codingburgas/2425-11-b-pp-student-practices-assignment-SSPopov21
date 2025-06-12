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
