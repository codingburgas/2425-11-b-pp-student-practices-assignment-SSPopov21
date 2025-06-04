from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SurveyForm(FlaskForm):
    years_experience = FloatField('Years of Experience', 
                                validators=[DataRequired(), NumberRange(min=0, max=50)])
    
    education_level = SelectField('Education Level',
                                choices=[(1, 'High School'), 
                                        (2, "Bachelor's Degree"),
                                        (3, "Master's Degree"),
                                        (4, 'PhD')],
                                coerce=int,
                                validators=[DataRequired()])
    
    num_skills = IntegerField('Number of Relevant Skills',
                             validators=[DataRequired(), NumberRange(min=0, max=100)])
    
    industry_type = SelectField('Industry Type',
                              choices=[('tech', 'Technology'),
                                     ('finance', 'Finance'),
                                     ('healthcare', 'Healthcare'),
                                     ('education', 'Education'),
                                     ('retail', 'Retail'),
                                     ('manufacturing', 'Manufacturing'),
                                     ('other', 'Other')],
                              validators=[DataRequired()])
    
    prev_job_changes = IntegerField('Number of Previous Job Changes',
                                   validators=[DataRequired(), NumberRange(min=0, max=20)])
    
    certifications = IntegerField('Number of Professional Certifications',
                                validators=[DataRequired(), NumberRange(min=0, max=20)])
    
    language_proficiency = FloatField('Language Proficiency (0-1)',
                                    validators=[DataRequired(), NumberRange(min=0, max=1)])
    
    interview_prep_score = FloatField('Interview Preparation Score (0-1)',
                                    validators=[DataRequired(), NumberRange(min=0, max=1)])
    
    success = BooleanField('Application Successful?')
    is_public = BooleanField('Make Results Public?')
    
    submit = SubmitField('Submit Survey') 