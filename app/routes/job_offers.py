from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app import db, mail
from app.models.job_offer import JobOffer
from app.models.survey import Survey
from app.forms.job_offer import JobOfferForm
from app.forms.job_application import JobApplicationForm
from app.ml.model import JobSuccessPredictor
import numpy as np
from flask_mail import Message

bp = Blueprint('job_offers', __name__)

@bp.route('/job-offers', methods=['GET'])
def list_jobs():
    """List all active job offers"""
    job_offers = JobOffer.query.filter_by(is_active=True).order_by(JobOffer.created_at.desc()).all()
    return render_template('job_offers/list.html', job_offers=job_offers)

@bp.route('/job-offers/new', methods=['GET', 'POST'])
@login_required
def create_job_offer():
    """Create a new job offer (employers only)"""
    if not current_user.is_employer():
        flash('Само работодатели могат да публикуват обяви.', 'error')
        return redirect(url_for('main.index'))
    
    form = JobOfferForm()
    if form.validate_on_submit():
        job_offer = JobOffer(
            employer_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            requirements=form.requirements.data,
            location=form.location.data,
            salary_range=form.salary_range.data,
            industry_type=form.industry_type.data,
            required_experience=form.required_experience.data,
            education_level=form.education_level.data
        )
        db.session.add(job_offer)
        db.session.commit()
        flash('Обявата е публикувана успешно!', 'success')
        return redirect(url_for('job_offers.list_jobs'))
    
    return render_template('job_offers/create.html', form=form)

@bp.route('/job-offers/<int:id>')
def view_job_offer(id):
    """View a specific job offer"""
    job_offer = JobOffer.query.get_or_404(id)
    return render_template('job_offers/view.html', job_offer=job_offer)

@bp.route('/job-offers/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job_offer(id):
    """Edit a job offer (owner only)"""
    job_offer = JobOffer.query.get_or_404(id)
    
    if job_offer.employer_id != current_user.id:
        flash('Нямате право да редактирате тази обява.', 'error')
        return redirect(url_for('job_offers.view_job_offer', id=id))
    
    form = JobOfferForm(obj=job_offer)
    if form.validate_on_submit():
        form.populate_obj(job_offer)
        db.session.commit()
        flash('Обявата е обновена успешно!', 'success')
        return redirect(url_for('job_offers.view_job_offer', id=id))
    
    return render_template('job_offers/edit.html', form=form, job_offer=job_offer)

@bp.route('/job-offers/<int:id>/toggle', methods=['POST'])
@login_required
def toggle_job_offer(id):
    """Toggle job offer active status (owner only)"""
    job_offer = JobOffer.query.get_or_404(id)
    
    if job_offer.employer_id != current_user.id:
        flash('Нямате право да променяте тази обява.', 'error')
        return redirect(url_for('job_offers.view_job_offer', id=id))
    
    job_offer.is_active = not job_offer.is_active
    db.session.commit()
    status = 'активирана' if job_offer.is_active else 'деактивирана'
    flash(f'Обявата е {status} успешно!', 'success')
    return redirect(url_for('job_offers.view_job_offer', id=id))

@bp.route('/job-offers/<int:id>/delete', methods=['POST'])
@login_required
def delete_job_offer(id):
    """Delete a job offer (owner only)"""
    job_offer = JobOffer.query.get_or_404(id)
    
    if job_offer.employer_id != current_user.id:
        flash('Нямате право да изтриете тази обява.', 'error')
        return redirect(url_for('job_offers.view_job_offer', id=id))
    
    db.session.delete(job_offer)
    db.session.commit()
    flash('Обявата е изтрита успешно!', 'success')
    return redirect(url_for('job_offers.list_jobs'))

@bp.route('/job-offers/<int:id>/apply', methods=['GET', 'POST'])
@login_required
def apply_job(id):
    """Apply for a job offer with prediction"""
    if not current_user.is_worker():
        flash('Само търсещи работа могат да кандидатстват за обяви.', 'error')
        return redirect(url_for('job_offers.list_jobs'))

    job_offer = JobOffer.query.get_or_404(id)
    if not job_offer.is_active:
        flash('Тази обява вече не е активна.', 'error')
        return redirect(url_for('job_offers.list_jobs'))

    form = JobApplicationForm()
    success_probability = None
    feature_importance = None
    prediction_available = False

    if form.validate_on_submit():
        # Create a survey object to use with the predictor
        survey_data = Survey(
            user_id=current_user.id,
            years_experience=form.years_experience.data,
            education_level=int(form.education_level.data),
            num_skills=len(form.skills.data.split(',')) if form.skills.data else 0,
            industry_type=form.industry_type.data,
            prev_job_changes=form.prev_job_changes.data,
            certifications=form.certifications.data,
            language_proficiency=int(form.language_proficiency.data) / 5.0,  # Normalize to 0-1
            interview_prep_score=form.interview_prep_score.data / 10.0,  # Normalize to 0-1
            job_offer_id=job_offer.id
        )

        # Get prediction
        predictor = JobSuccessPredictor()
        try:
            # Initialize model with some default data if not trained
            if not predictor.is_trained:
                # Create synthetic training data
                X = np.array([
                    [5, 3, 5, 2, 2, 0.6, 0.8],  # Successful candidate
                    [1, 1, 2, 0, 0, 0.2, 0.3],  # Unsuccessful candidate
                    [3, 2, 4, 1, 1, 0.4, 0.6],  # Moderate success
                    [7, 4, 6, 3, 3, 0.8, 0.9],  # Very successful
                    [2, 2, 3, 1, 1, 0.4, 0.5],  # Moderate success
                ])
                y = np.array([1, 0, 1, 1, 0])
                
                # Train the model with default data
                predictor.model.fit(X, y)
                predictor.scaler.fit(X)
                predictor.is_trained = True

            success_probability = predictor.predict(survey_data)
            feature_importance = predictor.get_feature_importance()
            prediction_available = True

            # Save the survey for future model training
            db.session.add(survey_data)
            db.session.commit()

            # Format the probability as a percentage with color coding
            probability_percent = success_probability * 100
            if probability_percent >= 70:
                color = 'green'
            elif probability_percent >= 40:
                color = 'orange'
            else:
                color = 'red'

            # Send email to employer if probability is over 60%
            if probability_percent >= 60:
                employer_email = job_offer.employer.email
                msg = Message(
                    subject=f"Нов кандидат с {probability_percent:.1f}% шанс за успех",
                    recipients=[employer_email],
                    body=f"Имате нов кандидат за вашата обява '{job_offer.title}'.\n\n"
                         f"Потребител: {current_user.username} (имейл: {current_user.email})\n"
                         f"Шанс за успех: {probability_percent:.1f}%\n\n"
                         f"Детайли на кандидатурата:\n"
                         f"Години опит: {form.years_experience.data}\n"
                         f"Образование: {form.education_level.data}\n"
                         f"Индустрия: {form.industry_type.data}\n"
                         f"Умения: {form.skills.data}\n"
                         f"Сертификати: {form.certifications.data}\n"
                         f"Ниво на език: {form.language_proficiency.data}\n"
                         f"Подготовка за интервю: {form.interview_prep_score.data}\n"
                         f"Брой предишни работни места: {form.prev_job_changes.data}\n"
                         f"Мотивационно писмо: {form.motivation_letter.data}\n"
                )
                try:
                    mail.send(msg)
                except Exception as e:
                    print(f"Email sending error: {str(e)}")

            flash(f'Шансът да бъдете нает е "{probability_percent:.1f}%"', 'success')
            return redirect(url_for('job_offers.list_jobs'))
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            db.session.rollback()  # Roll back the session on error
            flash('Възникна грешка при обработката на кандидатурата. Моля, опитайте отново.', 'error')

    return render_template('job_offers/apply.html',
                         job_offer=job_offer,
                         form=form,
                         success_probability=success_probability,
                         feature_importance=feature_importance,
                         prediction_available=prediction_available)

@bp.route('/quick-predict/<int:job_id>', methods=['GET'])
def quick_predict(job_id):
    """Get a quick prediction without filling the full application"""
    job = JobOffer.query.get_or_404(job_id)
    
    # Create a simple survey data object for prediction
    class SurveyData:
        def __init__(self):
            self.years_experience = 2  # Default to 2 years
            self.education_level = 2  # Default to Bachelor's degree
            self.num_skills = 3  # Default to 3 skills
            self.prev_job_changes = 1  # Default to 1 previous job
            self.certifications = 1  # Default to 1 certification
            self.language_proficiency = 0.6  # Default to intermediate
            self.interview_prep_score = 0.75  # Default to good preparation
    
    predictor = JobSuccessPredictor()
    survey_data = SurveyData()
    
    try:
        # Initialize model with default training data if not trained
        if not predictor.is_trained:
            # Create synthetic training data
            X = np.array([
                [5, 3, 5, 2, 2, 0.6, 0.8],  # Successful candidate
                [1, 1, 2, 0, 0, 0.2, 0.3],  # Unsuccessful candidate
                [3, 2, 4, 1, 1, 0.4, 0.6],  # Moderate success
                [7, 4, 6, 3, 3, 0.8, 0.9],  # Very successful
                [2, 2, 3, 1, 1, 0.4, 0.5],  # Moderate success
            ])
            y = np.array([1, 0, 1, 1, 0])
            
            # Train the model with default data
            predictor.model.fit(X, y)
            predictor.scaler.fit(X)
            predictor.is_trained = True
        
        # Convert survey data to feature vector
        features = np.array([[
            survey_data.years_experience,
            survey_data.education_level,
            survey_data.num_skills,
            survey_data.prev_job_changes,
            survey_data.certifications,
            survey_data.language_proficiency,
            survey_data.interview_prep_score
        ]])
        
        # Scale features if model is trained with a scaler
        if predictor.scaler:
            features = predictor.scaler.transform(features)
        
        success_probability = predictor.model.predict_proba(features)[0][1]
        
        return jsonify({
            'success': True,
            'probability': round(success_probability * 100, 1),
            'job_id': job_id,
            'redirect_url': url_for('job_offers.apply_job', id=job_id)
        })
    except Exception as e:
        print(f"Prediction error: {str(e)}")  # Log the error
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/predict', methods=['POST'])
def predict_success():
    data = request.get_json()
    skills = data.get('skills', [])
    
    # Create a simple survey data object for prediction
    class SurveyData:
        def __init__(self, skills):
            self.years_experience = 0  # Will be calculated based on skills
            self.education_level = 2  # Default to Bachelor's degree
            self.num_skills = len(skills)
            self.prev_job_changes = 0  # Default
            self.certifications = 0  # Default
            self.language_proficiency = 1  # Default to intermediate
            self.interview_prep_score = 75  # Default to good preparation
            
            # Calculate years of experience based on number of skills
            # Assuming more skills generally correlate with more experience
            self.years_experience = min(10, self.num_skills * 1.5)
    
    predictor = JobSuccessPredictor()
    survey_data = SurveyData(skills)
    
    try:
        success_probability = predictor.predict(survey_data)
        return jsonify({
            'success': True,
            'probability': round(success_probability * 100, 1),
            'message': f'Based on your skills, your estimated chance of being hired is {round(success_probability * 100, 1)}%'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 