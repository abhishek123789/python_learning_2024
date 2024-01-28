from flask import Flask
from .database_extensions import db
from datetime import datetime
from flask_restx import Api, Resource, Namespace
from .models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstdatabase.db'
db.init_app(app)
api = Api(app)

USER_NS = Namespace("User", description="REST services for User")

api.add_namespace(USER_NS)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     created = db.Column(db.DateTime, default=datetime.utcnow())

#     def __repr__(self):
#         return '<User %r>' % self.username



@USER_NS.route('/')
class hello_world(Resource):
    def post(self):
        user = User(username="Abhishek", email="abhishek123789@gmail.com")
        db.session.add(user)
        db.session.commit()
        return 'Hello, World!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    Api.init_app(app)

    app.run()

    