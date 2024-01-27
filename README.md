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
