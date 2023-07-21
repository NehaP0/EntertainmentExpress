# app/models/movie.py

from app import db  # Assuming you've already initialized 'db'

class Movie:
    def __init__(self, title, description, rating, cast):
        self.title = title
        self.description = description
        self.rating = rating
        self.cast = cast
        self.show_timings = []
        self.categories = []

    def save(self):
        db.movies.insert_one(self.__dict__)

    def delete(self):
        db.movies.delete_one({'_id': self._id})

    # Add methods to manage show timings and categories for the movie
    def add_show_timing(self, show_timing):
        self.show_timings.append(show_timing)

    def add_category(self, category):
        self.categories.append(category)

    @staticmethod
    def find():
        return list(db.movies.find())

    @staticmethod
    def find_one(filter):
        return db.movies.find_one(filter)
    
# In this code, we've added routes to get all movies, get a specific movie by ID, create a new movie, update an existing movie, and delete a movie. We've also implemented the corresponding CRUD operations in the Movie model to save, delete, and retrieve movie information from the database.
# Remember to test these routes using tools like Postman or cURL. You can get all movies by making a GET request to /movies, get a specific movie by ID by making a GET request to /movies/<movie_id>, create a new movie by making a POST request to /movies, update a movie by making a PUT request to /movies/<movie_id>, and delete a movie by making a DELETE request to /movies/<movie_id>.

# With these updates, we've added a route to get the show timings and categories for a movie. We've also added corresponding methods in the Movie model to add show timings and categories.
# You can get the show timings and categories for a movie by making a GET request to /shows/movies/<movie_id>