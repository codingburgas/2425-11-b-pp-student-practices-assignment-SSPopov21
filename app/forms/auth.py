from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional
from app.models.user import User

class LoginForm(FlaskForm):
    username = StringField('Потребителско име')
    admin_code = StringField('Код за администратор')
    password = PasswordField('Парола', validators=[DataRequired()])
    remember_me = BooleanField('Запомни ме')
    submit = SubmitField('Вход')

class RegistrationForm(FlaskForm):
    username = StringField('Потребителско име', validators=[Length(min=3, max=64)])
    email = StringField('Имейл', validators=[Email(), Length(max=120)])
    password = PasswordField('Парола', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Повтори паролата', validators=[EqualTo('password', message='Паролите трябва да съвпадат')])
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

class ProfileUpdateForm(FlaskForm):
    username = StringField('Потребителско име', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Имейл', validators=[DataRequired(), Email(), Length(max=120)])
    new_password = PasswordField('Нова парола', validators=[Optional(), Length(min=6)])
    new_password2 = PasswordField('Повтори новата парола', validators=[EqualTo('new_password', message='Паролите трябва да съвпадат')])
    submit = SubmitField('Запази промените')

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Това потребителско име вече е заето. Моля, изберете друго.')

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Този имейл адрес вече е регистриран.') 