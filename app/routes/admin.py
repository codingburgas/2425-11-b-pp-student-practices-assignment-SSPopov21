from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import User, JobApplication
from functools import wraps

bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You do not have permission to access this page.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    applications = JobApplication.query.all()
    return render_template('admin/dashboard.html', title='Admin Dashboard',
                         users=users, applications=applications)

@bp.route('/admin/user/<int:user_id>')
@login_required
@admin_required
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    return render_template('admin/user_details.html', title='User Details',
                         user=user, applications=applications)

@bp.route('/admin/user/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.role == 'admin':
        flash('Cannot delete admin users.')
        return redirect(url_for('admin.admin_dashboard'))
    
    # Delete user's applications first
    JobApplication.query.filter_by(user_id=user_id).delete()
    db.session.delete(user)
    db.session.commit()
    flash('User has been deleted.')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/admin/application/<int:app_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_application(app_id):
    application = JobApplication.query.get_or_404(app_id)
    db.session.delete(application)
    db.session.commit()
    flash('Application has been deleted.')
    return redirect(url_for('admin.admin_dashboard')) 