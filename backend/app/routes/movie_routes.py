# app/routes/movie_routes.py

from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.movie import Movie

# Create a blueprint for movie routes
bp = Blueprint('movie', __name__, url_prefix='/movies')


# Route to get all movies
@bp.route('/', methods=['GET'])
def get_all_movies():
    movies = Movie.find()
    return jsonify(movies), 200


# Route to get a specific movie by ID
@bp.route('/<movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    movie = Movie.find_one({'_id': ObjectId(movie_id)})

    if not movie:
        return jsonify({'message': 'Movie not found.'}), 404

    return jsonify(movie), 200


# Route to create a new movie
@bp.route('/', methods=['POST'])
def create_movie():
    data = request.get_json()

    # Extract movie details from the request data
    title = data.get('title')
    description = data.get('description')
    rating = data.get('rating')
    cast = data.get('cast')

    # Validate if required fields are provided
    if not title or not description or not rating:
        return jsonify({'message': 'Please provide all required fields.'}), 400

    # Create a new movie object
    new_movie = Movie(
        title=title,
        description=description,
        rating=rating,
        cast=cast
    )

    # Save the movie to the database
    new_movie.save()

    return jsonify({'message': 'Movie created successfully.', 'movie_id': str(new_movie['_id'])}), 201


# Route to update a movie by ID
@bp.route('/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()

    # Find the movie by ID
    movie = Movie.find_one({'_id': ObjectId(movie_id)})

    if not movie:
        return jsonify({'message': 'Movie not found.'}), 404

    # Update the movie fields based on the provided data
    movie.title = data.get('title', movie.title)
    movie.description = data.get('description', movie.description)
    movie.rating = data.get('rating', movie.rating)
    movie.cast = data.get('cast', movie.cast)

    # Save the updated movie to the database
    movie.save()

    return jsonify({'message': 'Movie updated successfully.'}), 200


# Route to delete a movie by ID
@bp.route('/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    # Find the movie by ID
    movie = Movie.find_one({'_id': ObjectId(movie_id)})

    if not movie:
        return jsonify({'message': 'Movie not found.'}), 404

    # Delete the movie from the database
    movie.delete()

    return jsonify({'message': 'Movie deleted successfully.'}), 200
