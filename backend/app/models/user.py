# app/models/user.py

from app import db  # Assuming you've already initialized 'db'
import re

class User(db.Model):
    def __init__(self, username, password, gender, membership_type, bio, date_of_birth):
        self.username = username
        self.password = password
        self.gender = gender
        self.membership_type = membership_type
        self.bio = bio
        self.date_of_birth = date_of_birth

    def save(self):
        db.users.insert_one(self.__dict__)

    def to_dict(self):
        user_dict = self.__dict__
        user_dict['_id'] = str(user_dict['_id'])
        return user_dict
    
    @staticmethod
    def find():
        return list(db.users.find())

    @staticmethod
    def find_one(filter):
        return db.users.find_one(filter)
