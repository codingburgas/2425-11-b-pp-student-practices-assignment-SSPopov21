from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from app.models.survey import Survey
from app.models.job_offer import JobOffer
from app.forms.auth import LoginForm, RegistrationForm
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

@bp.route('/profile')
@login_required
def profile():
    surveys_count = Survey.query.filter_by(user_id=current_user.id).count()
    return render_template('auth/profile.html', title='Профил', surveys_count=surveys_count)

@bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    try:
        # First delete all job offers if user is an employer
        if current_user.is_employer():
            JobOffer.query.filter_by(employer_id=current_user.id).delete()
            
        # Then delete user's surveys
        Survey.query.filter_by(user_id=current_user.id).delete()
        
        # Finally delete the user
        db.session.delete(current_user)
        db.session.commit()
        flash('Вашият профил беше изтрит успешно.')
        return redirect(url_for('main.index'))
    except Exception as e:
        db.session.rollback()
        flash('Възникна грешка при изтриването на профила. Моля, опитайте отново.')
        print(f"Account deletion error: {str(e)}")
        return redirect(url_for('auth.profile')) 