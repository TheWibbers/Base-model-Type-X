from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
#was __main__


@login_manager.user_loader
def load_patient(user_id):
    return Patient.query.get(int(user_id))

@login_manager.user_loader
def load_Doctor(user_id):
    return Doctor.query.get(int(user_id))


class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_username = db.Column(db.String(20),unique=False, nullable=False)
    patient_email = db.Column(db.String(50), unique=True, nullable=False)
    patient_password = db.Column(db.String(60), nullable=False)

    def __repr__(self): #how is printed out
        return f"Patient('{self.patient_username}', '{self.patient_email}')"

class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    doctor_username = db.Column(db.String(20),unique=False, nullable=False)
    doctor_email = db.Column(db.String(50), unique=True, nullable=False)
    doctor_password = db.Column(db.String(60), nullable=False)

    def __repr__(self): #how is printed out
        return f"Doctor('{self.doctor_username}', '{self.doctor_email}')"