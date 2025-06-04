from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.user import User
from app.models.survey import Survey
from functools import wraps

bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.admin:
            flash('You need to be an administrator to access this page.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    surveys = Survey.query.all()
    return render_template('admin/dashboard.html',
                         title='Admin Dashboard',
                         users=users,
                         surveys=surveys)

@bp.route('/user/<int:id>/delete')
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('You cannot delete your own admin account!')
        return redirect(url_for('admin.admin_dashboard'))
    
    # Delete user's surveys first
    Survey.query.filter_by(user_id=user.id).delete()
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} has been deleted.')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/user/<int:id>/toggle-role')
@login_required
@admin_required
def toggle_role(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('You cannot change your own role!')
        return redirect(url_for('admin.admin_dashboard'))
    
    user.role = 'admin' if user.role == 'student' else 'student'
    db.session.commit()
    flash(f'User {user.username} role changed to {user.role}.')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/survey/<int:id>/delete')
@login_required
@admin_required
def delete_survey(id):
    survey = Survey.query.get_or_404(id)
    db.session.delete(survey)
    db.session.commit()
    flash('Survey has been deleted.')
    return redirect(url_for('admin.admin_dashboard')) 