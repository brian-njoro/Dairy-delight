from .config import db
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

class Cattle(db.Model):
    serial_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    photo = db.Column(db.String(255))
    breed = db.Column(db.String(100))
    father = db.Column(db.Integer, db.ForeignKey('cattle.serial_number'))
    mother = db.Column(db.Integer, db.ForeignKey('cattle.serial_number'))
    method_bred = db.Column(db.String(100))


    #relationships
    dehorning = db.relationship('Dehorning', uselist=False, backref='cattle')
    treatments = db.relationship('Treatment', backref='cattle', lazy=True)
    pest_controls = db.relationship('PestControl', backref='cattle', lazy=True)
    periodic_treatments = db.relationship('PeriodicTreatment', backref='cattle', lazy=True)
    vaccinations = db.relationship('Vaccination', backref='cattle', lazy=True)