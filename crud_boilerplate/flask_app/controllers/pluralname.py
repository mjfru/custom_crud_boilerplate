from flask_app import app
from flask import # render_template, session, redirect, request, etc...
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# from flask_app.models.MODELNAME import CLASS


from flask_app.models.MODEL_FILE_NAME import ClassName
# Don't be like me, remember to change the 'modelfilename' to the actual file name...

# App Routes Go Below:

# Home Page / Read All
#@app.route("/")
# def ...():
#   variableToStoreAClass = Class.method()
#   return render_template("/...html", variableName = variableName)
                                        # Left of equal = Bucket, # Right of equal = Data
# Create 

# Read

# To read one instance / user / order etc...
# @app.route("/something/verb/<int:id>")
# def edit/change/etc(id):
#   user/order/thing = Class.get_something_by_id({'id': id})
#   return render_template("template.html", user/order/thing = user/order/thing)

# Update
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# Delete
