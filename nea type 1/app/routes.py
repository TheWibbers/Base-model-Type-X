#ROUTING FILE

#IMPORTS
import os
import secrets
from flask import render_template, url_for,flash, redirect, abort
from app import app, db, bcrypt
from app.models import User, Appointment #import 'User' Model from model.py
from app.forms import User_registrationform, LoginForm, app_book #Import forms for HTML pages (login and register)
from flask_login import login_user, current_user, logout_user, login_required #Flask login imports

db.create_all()

month_list = ['January','Febuary','March','April','May','June','July','August','September','November','December']

#ALL BELOW DOES NOT REQUIRE USER_AUTHENTIFICATON

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first() #quering database if username and email exists
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user) #logs user in
            email_check = User.query.filter_by(email=form.email.data).first()
            id_check = email_check.type_code
            if id_check == '0': #ID CHECK 0 = PATIENT
                return redirect(url_for('patient_hub'))
            if id_check == '1': #ID CHECK 1 = DOCTOR
                return redirect(url_for('doctor_hub'))
        else:
            flash('Login Unsuccessful. Check your email and password', 'danger') #infomation does not exist
    return render_template('login.html', title='login',form=form)

@app.route('/')
@app.route("/register",methods=['GET','POST'])
def register():
    form = User_registrationform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, type_code = form.type_code.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data} , an account has been created for you','success')
    return render_template('register.html',title='Register', form=form)


#ALL BELOW REQUIRES USER_AUTHENTIFICATON

#'@login_required' function checks user authentification.

@app.route("/appointment", methods=['GET', 'POST'])
@login_required
def appointment():
    form = app_book()
    if form.validate_on_submit():
        appointment = Appointment(month=form.month.data, date=form.date.data, time=form.time.data, message=form.message.data, author = current_user.email)
        if appointment.month in month_list:
            db.session.add(appointment)
            db.session.commit()
            flash(f'Appointment created','success')
        elif appointment.month not in month_list:
            flash(f'{form.month.data} is not a valid month','danger')

    return render_template('appointment.html', title = "Appointment book", form=form)


#@app.route("/appointment")
#@login_required
#def appointment():
    #return render_template('appointment.html')

#@app.route("/appointment/<appointment_id>")
#def appointment(appointment_id):
    #appointment = Appointment.query.get_or_404(appointment_id)
    #return render_template('appointment.html')

@app.route("/doctor_appointment")
@login_required
def doctor_appointment():
    appointments = Appointment.query.all()
    return render_template('doctor_appointment.html',title = "Appointments", appointments = appointments, month_list = ['January','Febuary','March','April','May','June','July','August','September','November','December'], month_number = 1)

@app.route("/patient_hub")
@login_required
def patient_hub():
    appointments = Appointment.query.all()
    return render_template('patient_hub.html', appointments = appointments)

@app.route("/doctor_hub")
@login_required
def doctor_hub():
    return render_template('doctor_hub.html')

@app.route("/message")
@login_required
def message():
    return render_template('message.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')