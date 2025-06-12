from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from app.models.survey import Survey
from app.models.job_offer import JobOffer
from app.forms.auth import LoginForm, RegistrationForm, ProfileUpdateForm
from app.ml.model import JobSuccessPredictor
from urllib.parse import urlparse

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Невалидно потребителско име или парола')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.dashboard')
        flash(f'Добре дошли, {user.username}!')
        return redirect(next_page)
    return render_template('auth/login.html', title='Вход', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Успешно излязохте от профила си.')
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                role=form.role.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Поздравления! Регистрацията е успешна.')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Възникна грешка при регистрацията. Моля, опитайте отново.')
            print(f"Registration error: {str(e)}")
            return redirect(url_for('auth.register'))
    return render_template('auth/register.html', title='Регистрация', form=form)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileUpdateForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.new_password.data:
            current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Промените са запазени успешно.')
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    # Get success prediction for workers
    success_probability = None
    feature_importance = None
    prediction_available = False
    
    if current_user.role == 'worker':
        # Get user's latest survey
        latest_survey = Survey.query.filter_by(user_id=current_user.id).order_by(Survey.created_at.desc()).first()
        if latest_survey:
            predictor = JobSuccessPredictor()
            try:
                success_probability = predictor.predict(latest_survey)
                feature_importance = predictor.get_feature_importance()
                prediction_available = True
            except Exception as e:
                print(f"Prediction error: {str(e)}")

    return render_template('auth/profile.html',
                         title='Профил',
                         form=form,
                         success_probability=success_probability,
                         feature_importance=feature_importance,
                         prediction_available=prediction_available)

@bp.route('/delete_profile')
@login_required
def delete_profile():
    try:
        # Delete user's surveys
        Survey.query.filter_by(user_id=current_user.id).delete()
        
        # Delete user's job offers if they're an employer
        if current_user.is_employer():
            JobOffer.query.filter_by(employer_id=current_user.id).delete()
        
        # Delete the user
        db.session.delete(current_user)
        db.session.commit()
        flash('Вашият профил беше изтрит успешно.')
        return redirect(url_for('main.index'))
    except Exception as e:
        db.session.rollback()
        flash('Възникна грешка при изтриването на профила. Моля, опитайте отново.')
        print(f"Profile deletion error: {str(e)}")
        return redirect(url_for('auth.profile')) 