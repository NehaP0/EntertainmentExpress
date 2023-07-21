# app/routes/user_routes.py

from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from app.models.user import User
import re

# Create a blueprint for user routes
bp = Blueprint('user', __name__, url_prefix='/users')


# Route for user signup (Registration)
@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Extract user details from the request data
    username = data.get('username')
    password = data.get('password')
    gender = data.get('gender')
    membership_type = data.get('membership_type')
    bio = data.get('bio')
    date_of_birth = data.get('date_of_birth')

    # Validate if required fields are provided
    if not username or not password or not gender or not membership_type or not date_of_birth:
        return jsonify({'message': 'Please provide all required fields.'}), 400

    # Check if the username is already taken
    existing_user = User.find_one({'username': username})
    if existing_user:
        return jsonify({'message': 'Username already exists. Please choose a different username.'}), 409

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password)

    # Create a new user object
    new_user = User(
        username=username,
        password=hashed_password,
        gender=gender,
        membership_type=membership_type,
        bio=bio,
        date_of_birth=date_of_birth
    )

    # Save the user to the database
    new_user.save()

    # Remove the password field from the response
    new_user_dict = new_user.to_dict()
    new_user_dict.pop('password', None)

    return jsonify({'message': 'User successfully registered.', 'user': new_user_dict}), 201


# Route for user login (Authentication)
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Extract user details from the request data
    username = data.get('username')
    password = data.get('password')

    # Validate if required fields are provided
    if not username or not password:
        return jsonify({'message': 'Please provide username and password.'}), 400

    # Find the user by username
    user = User.find_one({'username': username})

    # Check if the user exists and the password is correct
    if user and check_password_hash(user['password'], password):
        # Here, you can implement JWT authentication and return a token
        
        # Remove the password field from the response
        user.pop('password', None)
        return jsonify({'message': 'Login successful.', 'user': user}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401


# Route to get all users
@bp.route('/', methods=['GET'])
def get_all_users():
    # Get all users from the database
    users = User.find()

    # Convert the ObjectId to string for each user
    users = [{'_id': str(user['_id']), 'username': user['username'], 'user_status': user['user_status'],
              'gender': user['gender'], 'membership_type': user['membership_type'], 'bio': user['bio'],
              'date_of_birth': user['date_of_birth']} for user in users]

    return jsonify(users), 200

# Route to delete a user by ID
@bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Find the user by ID
    user = User.find_one({'_id': ObjectId(user_id)})

    if not user:
        return jsonify({'message': 'User not found.'}), 404

    # Delete the user from the database
    User.delete({'_id': ObjectId(user_id)})

    return jsonify({'message': 'User deleted successfully.'}), 200

# Route to get user profile by ID
@bp.route('/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    # Find the user by ID
    user = User.find_one({'_id': ObjectId(user_id)})

    if not user:
        return jsonify({'message': 'User not found.'}), 404

    # Remove the password field from the response
    user.pop('password', None)

    return jsonify(user), 200


# Route to update user profile by ID
@bp.route('/<user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.get_json()

    # Find the user by ID
    user = User.find_one({'_id': ObjectId(user_id)})

    if not user:
        return jsonify({'message': 'User not found.'}), 404

    # Update the user fields based on the provided data
    user.username = data.get('username', user.username)
    user.gender = data.get('gender', user.gender)
    user.membership_type = data.get('membership_type', user.membership_type)
    user.bio = data.get('bio', user.bio)
    user.date_of_birth = data.get('date_of_birth', user.date_of_birth)

    # Save the updated user to the database
    user.save()

    return jsonify({'message': 'User profile updated successfully.'}), 200
