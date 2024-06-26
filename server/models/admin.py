from .config import db 

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    farm_name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    # One-to-many relationship with cattle
    cattle = db.relationship('Cattle', backref='admin', lazy=True)
