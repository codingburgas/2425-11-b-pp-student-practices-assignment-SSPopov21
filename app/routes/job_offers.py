from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.models.job_offer import JobOffer
from app.forms.job_offer import JobOfferForm

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