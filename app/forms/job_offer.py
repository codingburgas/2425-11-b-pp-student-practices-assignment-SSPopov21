from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class JobOfferForm(FlaskForm):
    title = StringField('Заглавие на позицията', validators=[DataRequired(), Length(min=3, max=100)])
    description = TextAreaField('Описание на позицията', validators=[DataRequired()])
    requirements = TextAreaField('Изисквания', validators=[DataRequired()])
    location = StringField('Локация', validators=[DataRequired(), Length(max=100)])
    salary_range = StringField('Диапазон на заплатата', validators=[Length(max=100)])
    industry_type = SelectField('Индустрия', 
        choices=[
            ('IT', 'IT и Технологии'),
            ('Finance', 'Финанси и Банкиране'),
            ('Healthcare', 'Здравеопазване'),
            ('Education', 'Образование'),
            ('Manufacturing', 'Производство'),
            ('Retail', 'Търговия'),
            ('Other', 'Друго')
        ],
        validators=[DataRequired()]
    )
    required_experience = FloatField('Изискван опит (години)', 
        validators=[DataRequired(), NumberRange(min=0, max=50)]
    )
    education_level = SelectField('Изисквано образование',
        choices=[
            (1, 'Средно образование'),
            (2, 'Бакалавър'),
            (3, 'Магистър'),
            (4, 'Доктор')
        ],
        validators=[DataRequired()],
        coerce=int
    )
    submit = SubmitField('Публикувай обява') 