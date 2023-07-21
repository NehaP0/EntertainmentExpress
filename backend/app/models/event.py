# app/models/event.py

from app import db  # Assuming you've already initialized 'db'

class Event:
    def __init__(self, name, description, date, participants):
        self.name = name
        self.description = description
        self.date = date
        self.participants = participants

    def save(self):
        db.events.insert_one(self.__dict__)

    @staticmethod
    def find():
        return list(db.events.find())

    @staticmethod
    def find_one(filter):
        return db.events.find_one(filter)
    

    #In this code, we've added routes to get all events, get a specific event by ID, create a new event, and register a participant for an event. We've also implemented the corresponding functionality in the Event model to save and retrieve event information from the database.
    #You can get all events by making a GET request to /events, get a specific event by ID by making a GET request to /events/<event_id>, create a new event by making a POST request to /events, and register a participant for an event by making a POST request to /events/<event_id>/register