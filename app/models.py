from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='worker')  # worker, employer, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    applications = db.relationship('JobApplication', backref='applicant', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    years_experience = db.Column(db.Float, nullable=False)
    education_level = db.Column(db.Integer, nullable=False)  # 1-5 scale
    num_skills = db.Column(db.Integer, nullable=False)
    industry_type = db.Column(db.String(50), nullable=False)
    previous_success_rate = db.Column(db.Float, nullable=False)
    interview_score = db.Column(db.Float, nullable=False)
    success_probability = db.Column(db.Float)
    is_successful = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'years_experience': self.years_experience,
            'education_level': self.education_level,
            'num_skills': self.num_skills,
            'industry_type': self.industry_type,
            'previous_success_rate': self.previous_success_rate,
            'interview_score': self.interview_score,
            'success_probability': self.success_probability,
            'is_successful': self.is_successful,
            'created_at': self.created_at.isoformat()
        } 