from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import JobApplication
from app.forms import JobApplicationForm
from app.ml.logistic_regression import LogisticRegression
import numpy as np

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')

@bp.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    form = JobApplicationForm()
    if form.validate_on_submit():
        # Create feature vector
        features = np.array([[
            form.years_experience.data,
            form.education_level.data,
            form.num_skills.data,
            # Convert industry type to numeric
            {'tech': 0, 'finance': 1, 'healthcare': 2, 'education': 3, 'manufacturing': 4, 'other': 5}[form.industry_type.data],
            form.previous_success_rate.data / 100,  # Normalize to 0-1
            form.interview_score.data / 100  # Normalize to 0-1
        ]])
        
        # Get model predictions
        model = LogisticRegression()
        # TODO: Load trained model weights or train on historical data
        probability = model.predict_proba(features)[0]
        
        # Save application
        application = JobApplication(
            user_id=current_user.id,
            years_experience=form.years_experience.data,
            education_level=form.education_level.data,
            num_skills=form.num_skills.data,
            industry_type=form.industry_type.data,
            previous_success_rate=form.previous_success_rate.data,
            interview_score=form.interview_score.data,
            success_probability=probability
        )
        db.session.add(application)
        db.session.commit()
        
        flash(f'Success probability: {probability:.2%}')
        return redirect(url_for('main.results'))
    
    return render_template('apply.html', title='Apply', form=form)

@bp.route('/results')
@login_required
def results():
    applications = JobApplication.query.filter_by(user_id=current_user.id).order_by(JobApplication.created_at.desc()).all()
    return render_template('results.html', title='Results', applications=applications)

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile') 