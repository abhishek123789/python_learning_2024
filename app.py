from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstdatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    user = User(username="Abhishek", email="abhishek123789@gmail.com")
    db.session.add(user)
    db.session.commit()
    return 'Hello, World!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    