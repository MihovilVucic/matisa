from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

# Forma za login
class LoginForm(FlaskForm):
    username = StringField('Korisničko ime:', validators=[DataRequired()])
    password = PasswordField('Lozinka:', validators=[DataRequired()])
    remember_me = BooleanField('Zapamti me')
    submit = SubmitField('Prijava')

# Utility klasa, za next i back gumbe, možda kasnije iskorisiti za ispit ili nešto, sada beskorisna 
class BackNextForm(FlaskForm):
    back_button = SubmitField('Back')
    next_button = SubmitField('Next')

# Forma za registraciju
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    avatar = RadioField('Odaberi avatar:', choices=[('1', 'Dođ amo'),
                                     ('2', 'Gym bro'),('3', 'Casio me spasio'),
                                     ('4', 'Savršena hiperbola'),('5', 'zzzzz'),
                                     ('6', '...nisu tako strašni...'),('7', 'Tony Hawk')], validators=[validators.Optional()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Molim te izaberi drugo korisničko ime.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Molim te koristi drugu email adresu.')

# Forma za zahtjev za reset passa
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

# Forma za reset passa
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
