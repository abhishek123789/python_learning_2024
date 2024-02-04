import logging
from flask_restx import Resource, Namespace
from rest_app.services.api_models.user import user_model, USER_MODEL_PAYLOAD
# from rest_app.models.user import User as UserData
from rest_app.database_extensions import db
from flask import request
from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError
from rest_app.core.user import UserData

# This code snippet creates a logger object, which is a mechanism for recording events,
# errors, warnings, and other information during program execution.
logger = logging.getLogger(__name__)

USER_NS = Namespace("User", description="REST services for User")

@USER_NS.doc(responses={HTTPStatus.CREATED: "User Successfully created"})
@USER_NS.route('/')
class User(Resource):
    @USER_NS.expect(USER_MODEL_PAYLOAD)
    # @USER_NS.marshal_with(user_model)
    # @allowed_role_to_use_api
    def post(self):
        # username=USER_NS.payload["email"]
        # print(username)

        # print(kwargs)

        # Access request parameters
        # print(request.args)

        # Access request body
        # print(request.json)
        try:
            error = UserData(
                username=USER_NS.payload["username"],
                email=USER_NS.payload["email"]
            ).save()
            # breakpoint()
            if error:
                print(f"Errors are {error}")

            db.session.commit()

        except SQLAlchemyError as e:
            # Show what the error message is
            print(f"Error occurred while saving object: {e}")

        return "User Created", HTTPStatus.CREATED
