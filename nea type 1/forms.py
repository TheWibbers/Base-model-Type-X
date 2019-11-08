from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired , Length , EqualTo, Email

class patient_RegistrationForm(FlaskForm):
    patient_username = StringField('Full Real Name',
                           validators=[DataRequired(), Length(min=2,max=30)])
    patient_email = StringField('Email',
                        validators=[DataRequired(), Email()])
    patient_password = StringField('Password',
                           validators=[DataRequired()])
    patient_confirm_password = StringField('Confirm Password',
                                   validators=[DataRequired(),EqualTo('Password')])
    submit = SubmitField('Sign Up')

class doctor_RegistrationForm(FlaskForm):
    doctor_username = StringField('Full Real Name',
                           validators=[DataRequired(), Length(min=2,max=30)])
    doctor_email = StringField('Email',
                        validators=[DataRequired(), Email()])
    doctor_password = StringField('Password',
                           validators=[DataRequired()])
    doctor_confirm_password = StringField('Confirm Password',
                                   validators=[DataRequired(),EqualTo('Password')])
    doctor_code = StringField('Doctor ID code (Leave blank if a patient)',
                              validators=[Length(min=20,max=20)])
    submit = SubmitField('Sign Up')

class patient_LoginForm(FlaskForm):
    patient_email = StringField('Email',validators=[DataRequired(), Email()])
    patient_password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class doctor_LoginForm(FlaskForm):
    doctor_email = StringField('Email',validators=[DataRequired(), Email()])
    doctor_password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



