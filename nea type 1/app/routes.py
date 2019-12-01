from flask import render_template, url_for,flash, redirect
from app import app, db, bcrypt
from app.models import Patient, Doctor, Patient_Book
from app.forms import patient_RegistrationForm, doctor_RegistrationForm, patient_LoginForm,doctor_LoginForm, patient_Book_Form
from flask_login import LoginManager,login_user, current_user, logout_user, login_required
login_manager = LoginManager(app)

db.create_all()

#Homepage
@app.route('/')
@app.route("/homepage")
def home():
    return render_template('home.html')

#patient message
@app.route('/')
@app.route("/patient_message")
@login_required
def patient_message():
    return render_template('patient_message.html')

#doctor message
@app.route('/')
@app.route("/doctor_message")
def doctor_message():
    return render_template('doctor_message.html')

#doctor appointmentpage
@app.route('/')
@app.route("/doctor_appointment")
def doctor_appointment():
    return render_template('doctor_appointment.html')

#PatientHomePage
@app.route('/')
@app.route("/patient_home")
def patient_home():
    return render_template('patient_home.html')

#DoctorHomePage
@app.route('/')
@app.route("/doctor_home")
def doctor_home():
    return render_template('doctor_home.html')

#AboutPage
@app.route('/')
@app.route("/about")
def about():
    return render_template('about.html')

#Doctor help page
@app.route('/')
@app.route('/Doctor Help')
def doctor_help():
    return render_template('doctor_help.html')

#patient appointmentpage #########################
@app.route('/')
@app.route("/patient_appointment", methods=['GET','POST'])
def patient_appointment():
    form = patient_Book_Form()


#PatientLoginpage
@app.route('/')
@app.route("/login_patient", methods=['GET','POST'])
def login_patient():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = patient_LoginForm()

    if form.validate_on_submit():
        patient = Patient.query.filter_by(patient_email = form.patient_email.data).first()

        if patient and bcrypt.check_password_hash(patient.patient_password, form.patient_password.data):
            return redirect(url_for('patient_home')) #routes to patient homepage
        else:
            flash('Login Unsuccessful. Check your email and password', 'danger')

    return render_template('patient_login.html', title='login',form=form)

#DoctorLoginpage
@app.route('/')
@app.route("/login_doctor",methods=['GET','POST'])
def login_doctor():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
@app.route('/')
@app.route("/register_patient",methods=['GET','POST'])
def register_patient():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
@app.route('/')
@app.route("/register_doctor",methods=['GET','POST'])
def register_doctor():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = doctor_RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.doctor_password.data).decode('utf-8')
        doctor = Doctor(doctor_username = form.doctor_username.data, doctor_email = form.doctor_email.data, doctor_password = hashed_password)
        db.session.add(doctor)
        db.session.commit()
        flash(f'Account Created for {form.doctor_username.data}!','success')
        return redirect(url_for('login_doctor'))
    return render_template('register_doctor.html',title='Register',form=form)

@app.route("/account")
def account():
    return render_template('account.html', title='Account')
