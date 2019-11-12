from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired , Length , EqualTo, Email, ValidationError
from app.models import Patient, Doctor


class patient_RegistrationForm(FlaskForm):
    patient_username = StringField('Username', validators=[DataRequired(),Length(min=5,max=20)])
    patient_email = StringField('Email', validators=[DataRequired(), Email()])
    patient_password = StringField('Password', validators=[DataRequired()])
    patient_confirm_password = StringField('Confirm Password', validators=[DataRequired(),EqualTo('patient_password')])
    submit = SubmitField('Sign Up')
    
    #validation
    #def validate_username(Patient, patient_username):
        #newpatient = Patient.query.filter_by(patient_username = patient_username.data).first()
        #if newpatient:
            #raise ValidationError('The username you have chosen is already taken, please choose anther')


    def validate_email(Patient, patient_email): #validate_email
        patient = Patient.query.filter_by(patient_email = patient_email.data).first()
        if patient:
            raise ValidationError('The email you have chosen is already taken, please choose anther')

class doctor_RegistrationForm(FlaskForm):
    doctor_username = StringField('Username', validators=[DataRequired(), Length(min=5,max=20)])
    doctor_email = StringField('Email', validators=[DataRequired(), Email()])
    doctor_password = StringField('Password', validators=[DataRequired()])
    doctor_confirm_password = StringField('Confirm Password',validators=[DataRequired(),EqualTo('doctor_password')])
    submit = SubmitField('Sign Up')

    #validation
    #def validate_field(Doctor, doctor_username):
        #doctor = doctor.query.filter_by(doctor_username = doctor_username.data).first()
        #if doctor:
            #raise ValidationError('The username you have chosen is already taken, please choose anther')

    def validate_email(Doctor, doctor_email): #validate_email
        doctor = Doctor.query.filter_by(doctor_email = doctor_email.data).first()
        if doctor:
            raise ValidationError('The email you have chosen is already taken, please choose anther')


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


