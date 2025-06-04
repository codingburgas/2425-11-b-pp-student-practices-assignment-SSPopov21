from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models.user import User

class LoginForm(FlaskForm):
    username = StringField('Потребителско име', validators=[DataRequired()])
    password = PasswordField('Парола', validators=[DataRequired()])
    remember_me = BooleanField('Запомни ме')
    submit = SubmitField('Вход')

class RegistrationForm(FlaskForm):
    username = StringField('Потребителско име', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Имейл', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Парола', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Повтори паролата', validators=[DataRequired(), EqualTo('password', message='Паролите трябва да съвпадат')])
    role = SelectField('Тип потребител', choices=[
        ('worker', 'Търсещ работа'),
        ('employer', 'Работодател')
    ], validators=[DataRequired()])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Това потребителско име вече е заето. Моля, изберете друго.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Този имейл адрес вече е регистриран.') 