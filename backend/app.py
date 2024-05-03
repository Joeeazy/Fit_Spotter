from flask import Flask, request, abort
from config import  AppConfig
from flask.json import jsonify
from user_model import db, User
from flask_bcrypt import Bcrypt

app = Flask(__name__)
#get the configs
app.config.from_object(AppConfig)

#hashes passwords
bcrypt = Bcrypt(app)

#initialize app instance
db.init_app(app)

#push app context
with app.app_context():
    db.create_all()


# function to create a new user's account
@app.route("/register", methods=["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    #check if user exists with the email
    user_exists = User.query.filter_by(email=email).first() is not None #returns true if user exists

    #if user exists don't create account abort wwith status 409 conflict
    if user_exists:
        return jsonify({
            "error": "User already exists"
        }), 409

    #hash password using bcrypt
    hashed_password = bcrypt.generate_password_hash(password)

    #create new user with default id, email & hashed password
    new_user = User(email=email, password=hashed_password)

    #add the new user to our db
    db.session.add(new_user)
    db.session.commit()

    #return new_user's id and email
    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })

# function to login user
@app.route("/login", methods=["POST"])
def login_user():
    #get email & password
    email = request.json["email"]
    password = request.json["password"]

    #check if the user exists in the db
    user_exists = User.query.filter_by(email=email).first()  

    # if user doesnt exist return unauthorized with status code 401
    if user_exists is None:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    #else if the user exists check if passwords match!! if it doesn't match return unauth0rized
    if not bcrypt.check_password_hash(user_exists.password, password):
        return jsonify({
            "error": "Unauthorized"
            }), 401

    # if everything works return user
    return jsonify({
        "id": user_exists.id,
        "email": user_exists.email
    })

if(__name__) == "__main__":
    app.run(debug=True)