# app/routes/show_routes.py

from flask import Blueprint, jsonify
from app.models.movie import Movie

# Create a blueprint for show routes
bp = Blueprint('show', __name__, url_prefix='/shows')


# Route to get show timings and categories for a movie
@bp.route('/movies/<movie_id>', methods=['GET'])
def get_show_timings(movie_id):
    movie = Movie.find_one({'_id': ObjectId(movie_id)})

    if not movie:
        return jsonify({'message': 'Movie not found.'}), 404

    # Get the show timings and categories for the movie
    show_timings = movie.get('show_timings', [])
    categories = movie.get('categories', [])

    return jsonify({'show_timings': show_timings, 'categories': categories}), 200
