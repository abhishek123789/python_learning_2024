from flask import Flask
from .database_extensions import db
from datetime import datetime
from flask_restx import Api, Resource, Namespace
from .models.user import User
from .services.user import USER_NS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstdatabase.db'

db.init_app(app)
api = Api(app)

api.add_namespace(USER_NS)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()

    