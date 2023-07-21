from flask import Flask
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://neha:phadtare@cluster0.rw33h7h.mongodb.net/entertainmentexpress?retryWrites=true&w=majority"
mongo = PyMongo(app)

from app import routes