# Job Success Compass

A web-based system that predicts job application success probability using custom machine learning algorithms.

## Features

- Custom machine learning implementation using NumPy
- User registration and authentication
- Role-based access control (Student/Admin)
- Survey system for data collection
- Interactive visualization of results
- Profile management
- Model training interface

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
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

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:
```bash
flask run
```

## Project Structure

```
job-success-compass/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── forms/
│   ├── templates/
│   ├── static/
│   └── ml/
├── migrations/
├── instance/
├── tests/
├── requirements.txt
├── config.py
└── run.py
```

## Machine Learning Model

The system uses a custom implementation of logistic regression for predicting job application success. Features include:
- Years of experience
- Education level
- Number of skills
- Industry type
- Previous job changes
- Certifications
- Language proficiency
- Interview preparation score

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
