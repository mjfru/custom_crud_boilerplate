from flask_app.controllers import # Name of #! ALL controller file(s) here, no .py and seperated by a comma if more than one.
from flask_app import app

if __name__ == '__main__':
    app.run(debug = True)

# Commands to get this thing going in the terminal:
# python -m pipenv install flask PyMySQL (first time only)
# python -m pipenv install flask-bcrypt (first time only)
# python -m pipenv shell 
# python -m server.py