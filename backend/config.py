from dotenv import load_dotenv
import os
import redis

load_dotenv()

class AppConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]

    #set it to false to stop logging message
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #echo whats happening to the db
    SQLALCHEMY_ECHO = True

    #use Sqlite URI 
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"

    #sessions configs to help a user stay logged in
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")