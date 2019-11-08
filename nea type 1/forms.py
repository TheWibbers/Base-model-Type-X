from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired , Length , EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('Full Real Name',
                           validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired()])
    confirm_password = StringField('Confirm Password',
                                   validators=[DataRequired(),EqualTo('Password')])
    doctor_code = StringField('Doctor ID code (Leave blank if a patient)',
                              validators=[Length(min=20,max=20)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
