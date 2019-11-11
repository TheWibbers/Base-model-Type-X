from datetime import datetime
from app import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_username = db.Column(db.String(20),unique=True, nullable=False)
    patient_email = db.Column(db.String(50), unique=True, nullable=False)
    patient_password = db.Column(db.String(60), nullable=False)

    def __repr__(self): #how is printed out
        return f"Patient('{self.patient_username}', '{self.patient_email}')"

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_username = db.Column(db.String(20),unique=True, nullable=False)
    doctor_email = db.Column(db.String(50), unique=True, nullable=False)
    doctor_password = db.Column(db.String(60), nullable=False)
    idcode = db.Column(db.String(20),unique=True, nullable=False)

    def __repr__(self): #how is printed out
        return f"Doctor('{self.doctor_username}', '{self.doctor_email}', '{self.idcode}')"
