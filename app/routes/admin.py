from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.user import User
from app.models.survey import Survey
from functools import wraps
import os
from flask import current_app

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

@bp.route('/model/delete', methods=['POST'])
@login_required
@admin_required
def delete_model():
    """Delete the trained ML model and scaler files"""
    model_path = os.path.join(current_app.root_path, 'ml', 'job_success_model.pkl')
    scaler_path = os.path.join(current_app.root_path, 'ml', 'scaler.pkl')

    deleted_files = []
    errors = []

    if os.path.exists(model_path):
        try:
            os.remove(model_path)
            deleted_files.append('job_success_model.pkl')
        except OSError as e:
            errors.append(f'Error deleting job_success_model.pkl: {e}')
    else:
        errors.append('job_success_model.pkl not found.')

    if os.path.exists(scaler_path):
        try:
            os.remove(scaler_path)
            deleted_files.append('scaler.pkl')
        except OSError as e:
            errors.append(f'Error deleting scaler.pkl: {e}')
    else:
        errors.append('scaler.pkl not found.')

    if deleted_files:
        flash(f'Successfully deleted: {", ".join(deleted_files)}.', 'success')
    if errors:
        flash(f'Errors occurred: {", ".join(errors)}', 'error')
    
    return redirect(url_for('admin.admin_dashboard')) 