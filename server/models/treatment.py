from .config import db

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    cattle_serial_number = db.Column(db.Integer, db.ForeignKey('cattle.serial_number'))
    vet_name = db.Column(db.String(100))
    drug_used = db.Column(db.String(100))
    method_of_administration = db.Column(db.String(100))
    disease = db.Column(db.String(100))