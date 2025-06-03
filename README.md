# Job Application Success Predictor

A web-based system that predicts the probability of job application success based on user input data.

## Features

- User registration and authentication
- Role-based access (Worker, Employer, Admin)
- Job application form with ML-based success prediction
- Custom ML implementation using NumPy
- Data visualization
- Profile management
- Admin dashboard

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Project Structure

```
job_application_predictor/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── ml/
├── migrations/
├── instance/
├── .env
├── config.py
└── requirements.txt
```

## ML Model

The system uses a custom implementation of logistic regression for prediction, using the following features:
- Years of experience
- Education level
- Number of skills
- Industry type
- Previous job success rate
- Interview performance score

## License

MIT License 