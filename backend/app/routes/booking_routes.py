# app/routes/booking_routes.py

from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.booking import Booking
from app.models.movie import Movie
from app.models.event import Event

# Create a blueprint for booking routes
bp = Blueprint('booking', __name__, url_prefix='/bookings')


# Route to book tickets for a movie
@bp.route('/movies/<movie_id>', methods=['POST'])
def book_movie_tickets(movie_id):
    data = request.get_json()

    # Extract booking details from the request data
    show_time = data.get('show_time')
    num_seats = data.get('num_seats')

    # Validate if required fields are provided
    if not show_time or not num_seats:
        return jsonify({'message': 'Please provide show time and number of seats.'}), 400

    # Find the movie by ID
    movie = Movie.find_one({'_id': ObjectId(movie_id)})

    if not movie:
        return jsonify({'message': 'Movie not found.'}), 404

    # Calculate the total price based on the number of seats and show time
    # Replace this with your own logic based on pricing rules
    ticket_price = 10  # Assuming a static ticket price for simplicity
    total_price = ticket_price * num_seats

    # Create a new booking object
    new_booking = Booking(
        movie=movie_id,
        show_time=show_time,
        num_seats=num_seats,
        total_price=total_price
    )

    # Save the booking to the database
    new_booking.save()

    return jsonify({'message': 'Ticket booked successfully.', 'booking_id': str(new_booking['_id'])}), 201


# Route to book tickets for an event
@bp.route('/events/<event_id>', methods=['POST'])
def book_event_tickets(event_id):
    data = request.get_json()

    # Extract booking details from the request data
    num_tickets = data.get('num_tickets')

    # Validate if required fields are provided
    if not num_tickets:
        return jsonify({'message': 'Please provide the number of tickets.'}), 400

    # Find the event by ID
    event = Event.find_one({'_id': ObjectId(event_id)})

    if not event:
        return jsonify({'message': 'Event not found.'}), 404

    # Calculate the total price based on the number of tickets
    # Replace this with your own logic based on pricing rules
    ticket_price = 5  # Assuming a static ticket price for simplicity
    total_price = ticket_price * num_tickets

    # Create a new booking object
    new_booking = Booking(
        event=event_id,
        num_tickets=num_tickets,
        total_price=total_price
    )

    # Save the booking to the database
    new_booking.save()

    return jsonify({'message': 'Tickets booked successfully.', 'booking_id': str(new_booking['_id'])}), 201
