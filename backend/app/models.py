# models.py
from app import db

class User(db.Document):
      # Correct the field name to "_id"
    username = db.StringField(required=True)
    status = db.BooleanField(default=True)
    gender = db.StringField(choices=["Male", "Female", "Other"])
    membership_type = db.StringField(choices=["Regular", "Premium", "VIP"])
    bio = db.StringField()
    date_of_birth = db.DateField()

class Movie(db.Document):
      # Correct the field name to "_id"
    moviename = db.StringField(required=True)
    description = db.StringField(required=True)