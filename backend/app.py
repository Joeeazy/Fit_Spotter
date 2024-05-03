from flask import Flask
from config import  AppConfig
from user_model import db, User

app = Flask(__name__)
#get the configs
app.config.from_object(AppConfig)

#initialize app instance
db.init_app(app)

#push app context
with app.app_context():
    db.create_all()


if(__name__) == "__main__":
    app.run(debug=True)