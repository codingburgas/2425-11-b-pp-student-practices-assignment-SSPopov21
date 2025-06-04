from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.survey import Survey
from app.forms.survey import SurveyForm

bp = Blueprint('survey', __name__)

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_survey():
    # Redirect employers to job offer creation
    if current_user.is_employer():
        return redirect(url_for('job_offers.create_job_offer'))

    form = SurveyForm()
    if form.validate_on_submit():
        try:
            survey = Survey(
                user_id=current_user.id,
                years_experience=form.years_experience.data,
                education_level=form.education_level.data,
                num_skills=form.num_skills.data,
                industry_type=form.industry_type.data,
                prev_job_changes=form.prev_job_changes.data,
                certifications=form.certifications.data,
                language_proficiency=form.language_proficiency.data,
                interview_prep_score=form.interview_prep_score.data,
                success=form.success.data,
                is_public=form.is_public.data
            )
            db.session.add(survey)
            db.session.commit()
            flash('Анкетата е изпратена успешно!', 'success')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Възникна грешка при изпращането на анкетата. Моля, опитайте отново.', 'error')
            print(f"Error submitting survey: {str(e)}")
    
    return render_template('survey/new.html', title='Нова анкета', form=form) 