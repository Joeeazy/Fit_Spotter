from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]

    #set it to false to stop logging message
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #echo whats happening to the db
    SQLALCHEMY_ECHO = True

    #use Sqlite URI
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"