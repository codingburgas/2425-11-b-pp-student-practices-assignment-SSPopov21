from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.survey import Survey
from app.ml.model import JobSuccessPredictor
import numpy as np

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
    
    # Calculate probability for each survey
    predictor = JobSuccessPredictor()
    
    # Ensure the model is trained before making predictions for the dashboard
    try:
        if not predictor.is_trained:
            # Create synthetic training data if the model isn't trained yet
            X_synthetic = np.array([
                [5, 3, 5, 2, 2, 0.6, 0.8],  # Successful candidate
                [1, 1, 2, 0, 0, 0.2, 0.3],  # Unsuccessful candidate
                [3, 2, 4, 1, 1, 0.4, 0.6],  # Moderate success
                [7, 4, 6, 3, 3, 0.8, 0.9],  # Very successful
                [2, 2, 3, 1, 1, 0.4, 0.5],  # Moderate success
            ])
            y_synthetic = np.array([1, 0, 1, 1, 0])
            
            predictor.model.fit(X_synthetic, y_synthetic)
            predictor.scaler.fit(X_synthetic)
            predictor.is_trained = True
    except Exception as e:
        print(f"Dashboard model training error: {str(e)}")
        # Optionally, you could flash a message to the user here about the model not being ready

    for survey in user_surveys:
        try:
            probability = predictor.predict(survey)
            survey.probability_percent = probability * 100
        except Exception:
            survey.probability_percent = None

    # Get public surveys from other users
    public_surveys = Survey.query.filter(
        Survey.user_id != current_user.id,
        Survey.is_public == True
    ).all()
    
    # For employers: show candidates with >60% probability for their job offers
    top_candidates = []
    if current_user.is_employer():
        from app.models.job_offer import JobOffer
        my_offers = JobOffer.query.filter_by(employer_id=current_user.id).all()
        offer_ids = [offer.id for offer in my_offers]
        candidate_surveys = Survey.query.filter(Survey.job_offer_id.in_(offer_ids)).all() if offer_ids else []
        for survey in candidate_surveys:
            try:
                probability = predictor.predict(survey)
                if probability * 100 > 60:
                    survey.probability_percent = probability * 100
                    top_candidates.append(survey)
            except Exception:
                continue

    return render_template('main/dashboard.html',
                         title='Табло',
                         user_surveys=user_surveys,
                         public_surveys=public_surveys,
                         top_candidates=top_candidates) 