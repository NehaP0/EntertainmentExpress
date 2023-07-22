from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://neha:phadtare@cluster0.rw33h7h.mongodb.net/entertainmentexpress?retryWrites=true&w=majority"
mongo = PyMongo(app)

CORS(app)

from app import routes

# mongodb+srv://neha:phadtare@cluster0.rw33h7h.mongodb.net/entertainmentexpress?retryWrites=true&w=majority