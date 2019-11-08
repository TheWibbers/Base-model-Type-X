from flask import Flask, render_template, url_for,flash, redirect
from forms import patient_RegistrationForm, doctor_RegistrationForm, patient_LoginForm,doctor_LoginForm

app = Flask(__name__)

#Encryption Key
app.config['SECRET_KEY'] = 'jxtbgnrflzfqwcdsswxwahpcsdfpfehk'

#Homepage
@app.route('/')
@app.route("/homepage")
def home():
    return render_template('home.html')

#PatientLoginpage
@app.route('/')
@app.route("/login_patient",methods=['GET','POST'])
def login_patient():
    form = patient_LoginForm()
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
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register_patient.html',title='Register',form=form)

#Registerpage
@app.route("/register_doctor",methods=['GET','POST'])
def register_doctor():
    form = doctor_RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register_doctor.html',title='Register',form=form)


#Doctor help page
@app.route('/Doctor Help')
def doctor_help():
    return render_template('doctor_help.html')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
