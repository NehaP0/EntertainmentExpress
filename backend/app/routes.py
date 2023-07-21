from flask import jsonify, request
from bson import json_util
from app import app, mongo

# User endpoints
@app.route("/api/users", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find())
    return jsonify(json_util.dumps(users))

@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify(json_util.dumps(user))

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = {
        "username": data["username"],
        "status": data["status"],
        "gender": data["gender"],
        "membership_type": data["membership_type"],
        "bio": data["bio"],
        "date_of_birth": data["date_of_birth"]
    }
    result = mongo.db.users.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return jsonify(user), 201

@app.route("/api/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    updated_user = {
        "username": data["username"],
        "status": data["status"],
        "gender": data["gender"],
        "membership_type": data["membership_type"],
        "bio": data["bio"],
        "date_of_birth": data["date_of_birth"]
    }
    mongo.db.users.update_one({"_id": user_id}, {"$set": updated_user})
    return jsonify(updated_user)

@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": user_id})
    return jsonify({"message": "User deleted"})

# Movie and Show endpoints
@app.route("/api/movies", methods=["GET"])
def get_movies():
    movies = list(mongo.db.movies.find())
    return jsonify(json_util.dumps(movies))

@app.route("/api/movies/<movie_id>/shows", methods=["GET"])
def get_movie_shows(movie_id):
    shows = list(mongo.db.shows.find({"movie_id": movie_id}))
    return jsonify(json_util.dumps(shows))

@app.route("/api/movies", methods=["POST"])
def create_movie():
    data = request.get_json()
    movie = {
        "title": data["title"],
        "description": data["description"]
    }
    result = mongo.db.movies.insert_one(movie)
    movie["_id"] = str(result.inserted_id)
    return jsonify(movie), 201

@app.route("/api/movies/<movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    updated_movie = {
        "title": data["title"],
        "description": data["description"]
    }
    mongo.db.movies.update_one({"_id": movie_id}, {"$set": updated_movie})
    return jsonify(updated_movie)

@app.route("/api/movies/<movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    mongo.db.movies.delete_one({"_id": movie_id})
    return jsonify({"message": "Movie deleted"})

# Event and Participant endpoints
@app.route("/api/events", methods=["GET"])
def get_events():
    events = list(mongo.db.events.find())
    return jsonify(json_util.dumps(events))

@app.route("/api/events/<event_id>/participants", methods=["GET"])
def get_event_participants(event_id):
    participants = list(mongo.db.participants.find({"event_id": event_id}))
    return jsonify(json_util.dumps(participants))

@app.route("/api/events", methods=["POST"])
def create_event():
    data = request.get_json()
    event = {
        "title": data["title"],
        "description": data["description"]
    }
    result = mongo.db.events.insert_one(event)
    event["_id"] = str(result.inserted_id)
    return jsonify(event), 201

@app.route("/api/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.get_json()
    updated_event = {
        "title": data["title"],
        "description": data["description"]
    }
    mongo.db.events.update_one({"_id": event_id}, {"$set": updated_event})
    return jsonify(updated_event)

@app.route("/api/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    mongo.db.events.delete_one({"_id": event_id})
    return jsonify({"message": "Event deleted"})

# Show hierarchy endpoints
@app.route("/api/shows", methods=["GET"])
def get_shows():
    shows = list(mongo.db.shows.find())
    return jsonify(json_util.dumps(shows))

# Add more endpoints for show hierarchy as per your requirements