# app/db.py

from pymongo import MongoClient
from app import app

# Load configuration from config.py
app.config.from_pyfile('config.py')

# Connect to MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client['entertainmentexpress']

# 'mongodb://neha:phadtare@localhost:27017/entertainmentexpress'