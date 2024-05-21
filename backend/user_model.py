from flask_sqlalchemy import SQLAlchemy;
from uuid import uuid4

db = SQLAlchemy()

#get a unique id
def get_uuid():
    return uuid4().hex

# user schema class 
class User(db.Model):
    __tablename__ = "users"
    # default = unique id 
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    #email
    email = db.Column(db.String(345), unique=True)
    #password
    password = db.Column(db.Text, nullable=False)
