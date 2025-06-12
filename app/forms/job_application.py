from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class JobApplicationForm(FlaskForm):
    years_experience = IntegerField('Години опит', 
                                  validators=[DataRequired(), NumberRange(min=0, max=50)])
    education_level = SelectField('Образование',
                                choices=[
                                    (1, 'Основно'),
                                    (2, 'Средно'),
                                    (3, 'Бакалавър'),
                                    (4, 'Магистър'),
                                    (5, 'Доктор')
                                ],
                                validators=[DataRequired()])
    skills = TextAreaField('Умения (разделени със запетая)',
                          validators=[DataRequired(), Length(min=3, max=500)])
    certifications = IntegerField('Брой сертификати',
                                validators=[DataRequired(), NumberRange(min=0)])
    language_proficiency = SelectField('Ниво на владеене на чужди езици',
                                     choices=[
                                         (1, 'Начално'),
                                         (2, 'Средно'),
                                         (3, 'Напреднало'),
                                         (4, 'Свободно владеене'),
                                         (5, 'Майчин език')
                                     ],
                                     validators=[DataRequired()])
    interview_prep_score = IntegerField('Самооценка за подготовка за интервю (1-10)',
                                      validators=[DataRequired(), NumberRange(min=1, max=10)])
    prev_job_changes = IntegerField('Брой предишни работни места',
                                  validators=[DataRequired(), NumberRange(min=0)])
    motivation_letter = TextAreaField('Мотивационно писмо',
                                    validators=[DataRequired(), Length(min=100, max=2000)])
    submit = SubmitField('Кандидатствай')
