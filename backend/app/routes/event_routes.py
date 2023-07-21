# app/routes/event_routes.py

from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.event import Event

# Create a blueprint for event routes
bp = Blueprint('event', __name__, url_prefix='/events')


# Route to get all events
@bp.route('/', methods=['GET'])
def get_all_events():
    events = Event.find()
    return jsonify(events), 200


# Route to get a specific event by ID
@bp.route('/<event_id>', methods=['GET'])
def get_event_by_id(event_id):
    event = Event.find_one({'_id': ObjectId(event_id)})

    if not event:
        return jsonify({'message': 'Event not found.'}), 404

    return jsonify(event), 200


# Route to create a new event
@bp.route('/', methods=['POST'])
def create_event():
    data = request.get_json()

    # Extract event details from the request data
    name = data.get('name')
    description = data.get('description')
    date = data.get('date')
    participants = []

    # Validate if required fields are provided
    if not name or not date:
        return jsonify({'message': 'Please provide all required fields.'}), 400

    # Create a new event object
    new_event = Event(
        name=name,
        description=description,
        date=date,
        participants=participants
    )

    # Save the event to the database
    new_event.save()

    return jsonify({'message': 'Event created successfully.', 'event_id': str(new_event['_id'])}), 201


# Route to register a participant for an event
@bp.route('/<event_id>/register', methods=['POST'])
def register_participant(event_id):
    data = request.get_json()

    # Extract participant details from the request data
    participant_name = data.get('participant_name')

    # Find the event by ID
    event = Event.find_one({'_id': ObjectId(event_id)})

    if not event:
        return jsonify({'message': 'Event not found.'}), 404

    # Add the participant to the event's participants list
    event.participants.append(participant_name)

    # Save the updated event to the database
    event.save()

    return jsonify({'message': 'Participant registered successfully.'}), 200
