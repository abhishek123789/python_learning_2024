# python_learning_2024
check version of python - python3 --version

<!-- Create an environment -->
python3 -m venv .venv

<!-- Activate the environment -->
. .venv/bin/activate

<!-- Then you can install the depencies you want -->
pip install flask
pip install SQLAlchemy
pip install Flask-SQLAlchemy
pip install flask-restx 
<!-- In our app we are using restx for documentation, works as a swagger -->

<!-- This command will create a requirements.txt file in your current directory containing a list of all installed packages and their versions. -->
pip freeze > requirements.txt

<!-- What is the folder structure till now? -->
Models of Tables: In Flask, models of tables are often defined using an Object-Relational Mapper (ORM) such as SQLAlchemy. These models define the structure of your database tables and establish relationships between them. Each model typically corresponds to a table in your database and defines attributes that map to columns in the table.

API Models: API models in Flask represent the structure of data exchanged between the client and server in API requests and responses. They define the format of data expected by the API endpoints and returned by them. API models are not directly related to database tables but rather represent the structure of data that is transmitted over HTTP.

<!-- To print the payload you can use like this  -->
class hello_world(Resource):
    @USER_NS.expect(USER_MODEL_PAYLOAD)
    def post(self):
        print(USER_NS.payload)
        return {}