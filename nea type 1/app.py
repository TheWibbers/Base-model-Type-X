from flask import Flask, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#Encryption Key
app.config['SECRET_KEY'] = 'jxtbgnrflzfqwcdsswxwahpcsdfpfehk'


#Homepage
@app.route('/')
@app.route("/homepage")
def home():
    return render_template('home.html')

#Loginpage
@app.route('/')
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login',form=form)

#Registerpage
@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


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
