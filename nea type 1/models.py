from datetime import datetime
from __main__ import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _patient_username = db.Column(db.String(20),unique=True, nullable=False)
    _patient_email = db.Column(db.String(50), unique=True, nullable=False)
    _patient_password = db.Column(db.String(60), nullable=False)

    def __repr__(self): #how is printed out
        return f"Patient('{self._patient_username}', '{self._patient_email}')"

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _doctor_username = db.Column(db.String(20),unique=True, nullable=False)
    _doctor_email = db.Column(db.String(50), unique=True, nullable=False)
    _doctor_password = db.Column(db.String(60), nullable=False)
    _idcode = db.Column(db.String(20),unique=True, nullable=False)

    def __repr__(self): #how is printed out
        return f"Doctor('{self._doctor_username}', '{self._doctor_email}', '{self._idcode}"
