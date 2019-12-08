from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    type_code = db.Column(db.String(10), unique=False,nullable=True) #does not need to input
    password = db.Column(db.String(60), nullable=False)
    #appointments = db.relationship('Appointment', backref='author', lazy=True)
    
    def __repr__(self): 
        return f"Patient('{self.username}', '{self.email}', '{self.type_code}')"

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20),unique=False, nullable=False)
    date = db.Column(db.String(50), unique=False, nullable=False)
    time = db.Column(db.String(10), unique=False,nullable=False) 
    message = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String(60))
    #user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable = False)


    
    def __repr__(self): 
        return f"Patient('{self.month}', '{self.date}', '{self.time}','{self.message}')"
