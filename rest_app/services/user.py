from flask_restx import Resource, Namespace

USER_NS = Namespace("User", description="REST services for User")

@USER_NS.route('/')
class hello_world(Resource):
    def post(self):
        return {"Hello": "Hi"}