from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired , Length , EqualTo, Email, ValidationError
from app.models import User, Appointment

month_list = ['January','Febuary','March','April','May','June','July','August','September','November','December']

class User_registrationform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    type_code = BooleanField('I am a Medical Official',default=False)
    submit = SubmitField('Sign Up')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('The email you have chosen is already taken, please choose anther')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me',default=False)
    submit = SubmitField('Login')


class app_book(FlaskForm):
    month = StringField('Month',validators=[DataRequired()])
    date = StringField('Day',validators=[DataRequired()])
    time = StringField('Time',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])
    submit = SubmitField('Seek Appointment')

#class app_book(FlaskForm):
    #month = SelectField('Month',validators=[DataRequired()], choices=[('January','Febuary','March','April','May','June','July','August','September','November','December')])
    #date = SelectField('Day',validators=[DataRequired()],choices=[('1','2','3','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29')])
    #time = StringField('Time 24 Clock',validators=[DataRequired()])
    #message = TextAreaField('Message',validators=[DataRequired()])
    #submit = SubmitField('Seek Appointment')

