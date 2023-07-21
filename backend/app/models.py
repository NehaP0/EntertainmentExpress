from app import db

class User(db.Document):
    username = db.StringField(required=True)
    status = db.BooleanField(default=True)
    gender = db.StringField(choices=["Male", "Female", "Other"])
    membership_type = db.StringField(choices=["Regular", "Premium", "VIP"])
    bio = db.StringField()
    date_of_birth = db.DateField()

# 5de4tAfbQ8drhQoS