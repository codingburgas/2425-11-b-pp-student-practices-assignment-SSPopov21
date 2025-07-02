from app import db
from datetime import datetime

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_public = db.Column(db.Boolean, default=False)
    success = db.Column(db.Boolean)  # Target variable (successful application or not)
    job_offer_id = db.Column(db.Integer, db.ForeignKey('job_offer.id'), nullable=True)
    
    # Features
    years_experience = db.Column(db.Float, nullable=False)
    education_level = db.Column(db.Integer, nullable=False)  # 1: High School, 2: Bachelor's, 3: Master's, 4: PhD
    num_skills = db.Column(db.Integer, nullable=False)
    industry_type = db.Column(db.String(50), nullable=False)
    prev_job_changes = db.Column(db.Integer, nullable=False)
    certifications = db.Column(db.Integer, nullable=False)
    language_proficiency = db.Column(db.Float, nullable=False)  # Scale of 0-1
    interview_prep_score = db.Column(db.Float, nullable=False)  # Scale of 0-1
    
    def to_feature_vector(self):
        """Convert survey data to feature vector for ML model"""
        return [
            self.years_experience,
            self.education_level,
            self.num_skills,
            self.prev_job_changes,
            self.certifications,
            self.language_proficiency,
            self.interview_prep_score,
        ]
    
    def __repr__(self):
        return f'<Survey {self.id} by User {self.user_id}>' 