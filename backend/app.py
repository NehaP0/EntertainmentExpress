from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Load configuration from config.py

# Set up the MongoDB connection using pymongo
# Replace 'your_mongodb_uri' with the actual URI of your MongoDB database
mongo_client = MongoClient('your_mongodb_uri')
db = mongo_client.get_database('entertainmentexpress')  # Replace 'entertainmentexpress' with your database name

# Import and register the routes from the "routes" folder
from app.routes import user_routes, movie_routes, show_routes, event_routes

app.register_blueprint(user_routes.bp)
app.register_blueprint(movie_routes.bp)
app.register_blueprint(show_routes.bp)
app.register_blueprint(event_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)
