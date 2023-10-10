from flask import Flask
from flask_migrate import Migrate
from config import DataBaseConfig
from library_management.models import db, Book


app = Flask(__name__)
app.config.from_object(DataBaseConfig)
db.init_app(app)
migrate = Migrate(app, db)