from flask_restx import Resource, Namespace
from rest_app.services.api_models.user import user_model, USER_MODEL_PAYLOAD
from rest_app.models.user import User as UserData
from rest_app.database_extensions import db

USER_NS = Namespace("User", description="REST services for User")

@USER_NS.route('/')
class User(Resource):
    @USER_NS.expect(USER_MODEL_PAYLOAD)
    @USER_NS.marshal_with(user_model)
    def post(self):
        # username=USER_NS.payload["email"]
        # print(username)
        user = UserData(
            username=USER_NS.payload["username"],
            email=USER_NS.payload["email"]
        )
        # breakpoint()
        db.session.add(user)
        db.session.commit()
        return user, 201