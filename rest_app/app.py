from flask import Flask
# from .database_extensions import db
from datetime import datetime
from flask_restx import Resource, Namespace
from .models.user import User
from .services.user import USER_NS
from rest_app.database_extensions import db, api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstdatabase.db'

db.init_app(app)
api.init_app(app)

api.add_namespace(USER_NS)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()

    