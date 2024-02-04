import attr
from rest_app.models.user import User
from rest_app.core.base import IdMixin

@attr.s
class UserData(IdMixin):
    username: str = attr.ib(default=None)
    email: str = attr.ib(default=None)

    def save(self):
        # Logic to save UserData instance to the database or perform other actions
        print(f"Saving user data for {self.username} with email {self.email}")
        self.set_id(self.to_model())


    def to_model(self) -> User:
        return User(
            username=self.username,
            email=self.email
        )