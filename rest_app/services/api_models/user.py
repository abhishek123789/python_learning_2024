from flask_restx import fields
from rest_app.database_extensions import api

user_model = api.model('User', {
    "id": fields.Integer(description="User ID"),
    "username": fields.String(description="Username of the user"),
    "email": fields.String(description="Email address of the user")
})