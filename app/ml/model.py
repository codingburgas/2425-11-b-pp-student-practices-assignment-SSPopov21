import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

class JobSuccessPredictor:
    def __init__(self):
        self.model = LogisticRegression(random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        self.model_path = os.path.join(os.path.dirname(__file__), 'job_success_model.pkl')
        self.scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

    def prepare_features(self, surveys):
        """Convert survey data to feature matrix"""
        features = []
        targets = []
        
        for survey in surveys:
            feature_vector = [
                survey.years_experience,
                survey.education_level,
                survey.num_skills,
                survey.prev_job_changes,
                survey.certifications,
                survey.language_proficiency,
                survey.interview_prep_score
            ]
            features.append(feature_vector)
            targets.append(1 if survey.success else 0)
        
        return np.array(features), np.array(targets)

    def train(self, surveys):
        """Train the model on survey data"""
        if not surveys:
            raise ValueError("No training data provided")

        # Prepare features and targets
        X, y = self.prepare_features(surveys)
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train the model
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        # Save the model and scaler
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)
        
        self.is_trained = True
        return accuracy, report

    def predict(self, survey_data):
        """Predict success probability for new survey data"""
        if not self.is_trained:
            if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
                self.model = joblib.load(self.model_path)
                self.scaler = joblib.load(self.scaler_path)
                self.is_trained = True
            else:
                raise ValueError("Model not trained yet")

        # Prepare single survey data
        features = np.array([[
            survey_data.years_experience,
            survey_data.education_level,
            survey_data.num_skills,
            survey_data.prev_job_changes,
            survey_data.certifications,
            survey_data.language_proficiency,
            survey_data.interview_prep_score
        ]])
        
        # Scale features
        features_scaled = self.scaler.transform(features)
        
        # Get prediction probability
        prob = self.model.predict_proba(features_scaled)[0][1]
        return prob

    def get_feature_importance(self):
        """Get the importance of each feature in the model"""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
            
        feature_names = [
            'Years of Experience',
            'Education Level',
            'Number of Skills',
            'Previous Job Changes',
            'Certifications',
            'Language Proficiency',
            'Interview Preparation'
        ]
        
        coefficients = self.model.coef_[0]
        importance = dict(zip(feature_names, abs(coefficients)))
        return dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))

def prepare_data(surveys):
    """Convert survey data to numpy arrays for training"""
    X = np.array([survey.to_feature_vector() for survey in surveys])
    y = np.array([1 if survey.success else 0 for survey in surveys])
    return X, y

def normalize_features(X):
    """Normalize features to have zero mean and unit variance"""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std, mean, std 