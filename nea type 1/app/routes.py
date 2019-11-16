from flask import render_template, url_for,flash, redirect
from app import app, db, bcrypt
from app.models import Patient, Doctor
from app.forms import patient_RegistrationForm, doctor_RegistrationForm, patient_LoginForm,doctor_LoginForm
from flask_login import LoginManager
login_manager = LoginManager(app)

db.create_all()

#Homepage
@app.route('/')
@app.route("/homepage")
def home():
    return render_template('home.html')

#AboutPage
@app.route('/')
@app.route("/about")
def about():
    return render_template('about.html')

#PatientLoginpage
@app.route("/login_patient", methods=['GET','POST'])
def login_patient():
    form = patient_LoginForm()

    if form.validate_on_submit():
        patient = Patient.query.filter_by(patient_email = form.patient_email.data).first()

        if patient and bcrypt.check_password_hash(patient.patient_password, form.patient_password.data):
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check your email and password', 'danger')

    return render_template('patient_login.html', title='login',form=form)

#DoctorLoginpage
@app.route("/login_doctor",methods=['GET','POST'])
def login_doctor():
    form = doctor_LoginForm()

    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(doctor_email = form.doctor_email.data).first()

        if doctor and bcrypt.check_password_hash(doctor.doctor_password, form.doctor_password.data):
            return redirect(url_for('home'))
            flash('Login successful.', 'success')
        else:
            flash('Login Unsuccessful. Check your email and password', 'danger')

    return render_template('doctor_login.html', title='login',form=form)
    


#Registerpage
@app.route("/register_patient",methods=['GET','POST'])
def register_patient():
    form = patient_RegistrationForm()
    if form.validate_on_submit():
        flash(f'Welcome {form.patient_username.data} , an account has been created for you','success')
        hashed_password = bcrypt.generate_password_hash(form.patient_password.data).decode('utf-8')
        patient = Patient(patient_username = form.patient_username.data, patient_email = form.patient_email.data, patient_password = hashed_password)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('login_patient'))
    return render_template('register_patient.html',title='Register', form=form)

#Registerpage
@app.route("/register_doctor",methods=['GET','POST'])
def register_doctor():
    form = doctor_RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.doctor_password.data).decode('utf-8')
        doctor = Doctor(doctor_username = form.doctor_username.data, doctor_email = form.doctor_email.data, doctor_password = hashed_password)
        db.session.add(doctor)
        db.session.commit()
        flash(f'Account Created for {form.doctor_username.data}!','success')
        return redirect(url_for('login_doctor'))
    return render_template('register_doctor.html',title='Register',form=form)


#Doctor help page
@app.route('/Doctor Help')
def doctor_help():
    return render_template('doctor_help.html')