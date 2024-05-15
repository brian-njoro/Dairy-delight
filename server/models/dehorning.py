from .config import db

class Dehorning(db.Model):
    dehorning_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    cattle_serial_number = db.Column(db.Integer, db.ForeignKey('cattle.serial_number'))
    vet_name = db.Column(db.String(100))
    method = db.Column(db.String(100))