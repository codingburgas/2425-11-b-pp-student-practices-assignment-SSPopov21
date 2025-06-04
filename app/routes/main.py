from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.survey import Survey

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html', title='Home')

@bp.route('/dashboard')
@login_required
def dashboard():
    # Get user's surveys
    user_surveys = Survey.query.filter_by(user_id=current_user.id).all()
    
    # Get public surveys from other users
    public_surveys = Survey.query.filter(
        Survey.user_id != current_user.id,
        Survey.is_public == True
    ).all()
    
    return render_template('main/dashboard.html',
                         title='Табло',
                         user_surveys=user_surveys,
                         public_surveys=public_surveys) 