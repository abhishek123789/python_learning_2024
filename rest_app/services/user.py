from flask_restx import Resource, Namespace
from rest_app.services.api_models.user import user_model

USER_NS = Namespace("User", description="REST services for User")

@USER_NS.route('/')
class hello_world(Resource):
    @USER_NS.expect(user_model)
    def post(self):
        return {}