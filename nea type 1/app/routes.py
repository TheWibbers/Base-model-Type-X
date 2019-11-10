from flask import render_template, url_for,flash, redirect
from app import app, db, bcrypt
from app.models import Patient, Doctor
from app.forms import patient_RegistrationForm, doctor_RegistrationForm, patient_LoginForm,doctor_LoginForm



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
@app.route('/')
@app.route("/login_patient",methods=['GET','POST'])
def login_patient():
    form = patient_LoginForm()
    if form.validate_on_submit():
        if form.patient_email.data == 'samuelthomas342@yahoo.co.uk' and form.patient_password.data == 'password':
            flash('Logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check input details','danger')

    return render_template('patient_login.html', title='login',form=form)

#DoctorLoginpage
@app.route('/')
@app.route("/login_doctor",methods=['GET','POST'])
def login_doctor():
    form = doctor_LoginForm()
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
        flash('Your account has been created', 'success')
        return redirect(url_for('patient_login'))
    return render_template('register_patient.html',title='Register', form=form)

#Registerpage
@app.route("/register_doctor",methods=['GET','POST'])
def register_doctor():
    form = doctor_RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.doctor_username.data}!','success')
        hashed_password = bcrypt.generate_password_hash(form.patient_password.data).decode('utf-8')
        doctor = Doctor(doctor_username = form.doctor_username.data, doctor_email = form.doctor_email.data, doctor_password = hashed_password)
        db.session.add(doctor)
        db.session.commit()
        flash('Your account has been created','success')
        return redirect(url_for('doctor_login'))
    return render_template('register_doctor.html',title='Register',form=form)


#Doctor help page
@app.route('/Doctor Help')
def doctor_help():
    return render_template('doctor_help.html')