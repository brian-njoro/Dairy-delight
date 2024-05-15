from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.admin import Admin
from models.cattle import Cattle
from models.customer import Customer
from models.dehorning import Dehorning
# from models.deworming import Deworming
from models.equipment import Equipment
from models.inventory import Inventory
from models.payment import Payment
from models.periodic import PeriodicTreatment
from models.pestControl import PestControl
from models.product import Product
from models.worker import Worker
from models.vaccination import Vaccination
from models.treatment import Treatment
from models.rawmaterials import RawMaterial



from models.config import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)