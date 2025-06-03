from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('worker', 'Worker'), ('employer', 'Employer')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class JobApplicationForm(FlaskForm):
    years_experience = FloatField('Years of Experience', 
                                validators=[DataRequired(), NumberRange(min=0, max=50)])
    education_level = SelectField('Education Level',
                                choices=[(1, 'High School'),
                                        (2, 'Associate Degree'),
                                        (3, 'Bachelor Degree'),
                                        (4, 'Master Degree'),
                                        (5, 'PhD')],
                                coerce=int)
    num_skills = IntegerField('Number of Skills',
                            validators=[DataRequired(), NumberRange(min=1, max=50)])
    industry_type = SelectField('Industry Type',
                              choices=[('tech', 'Technology'),
                                      ('finance', 'Finance'),
                                      ('healthcare', 'Healthcare'),
                                      ('education', 'Education'),
                                      ('manufacturing', 'Manufacturing'),
                                      ('other', 'Other')])
    previous_success_rate = FloatField('Previous Job Application Success Rate (%)',
                                     validators=[DataRequired(), NumberRange(min=0, max=100)])
    interview_score = FloatField('Interview Performance Score (0-100)',
                               validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Predict Success Probability') 