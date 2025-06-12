from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.models.job_offer import JobOffer
from app.models.survey import Survey
from app.forms.job_offer import JobOfferForm
from app.forms.job_application import JobApplicationForm
from app.ml.model import JobSuccessPredictor

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
            num_skills=len(form.skills.data.split(',')),
            prev_job_changes=form.prev_job_changes.data,
            certifications=form.certifications.data,
            language_proficiency=int(form.language_proficiency.data),
            interview_prep_score=form.interview_prep_score.data
        )

        # Get prediction
        predictor = JobSuccessPredictor()
        try:
            success_probability = predictor.predict(survey_data)
            feature_importance = predictor.get_feature_importance()
            prediction_available = True

            # Save the survey for future model training
            db.session.add(survey_data)
            db.session.commit()

            flash(f'Вашата кандидатура е изпратена успешно! Вероятност за одобрение: {success_probability:.1%}', 'success')
            return redirect(url_for('job_offers.list_jobs'))
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            flash('Възникна грешка при обработката на кандидатурата. Моля, опитайте отново.', 'error')

    return render_template('job_offers/apply.html',
                         job_offer=job_offer,
                         form=form,
                         success_probability=success_probability,
                         feature_importance=feature_importance,
                         prediction_available=prediction_available) 