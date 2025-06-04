from app import db
from datetime import datetime

class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary_range = db.Column(db.String(100))
    industry_type = db.Column(db.String(50), nullable=False)
    required_experience = db.Column(db.Float, nullable=False)
    education_level = db.Column(db.Integer, nullable=False)  # 1: High School, 2: Bachelor's, 3: Master's, 4: PhD
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    employer = db.relationship('User', backref='job_offers')
    
    def __repr__(self):
        return f'<JobOffer {self.title} by {self.employer.username}>' 