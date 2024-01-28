from flask_restx import fields

user_model = {
    "id": fields.Integer(description="User ID"),
    "username": fields.String(description="Username of the user"),
    "email": fields.String(description="Email address of the user")
}