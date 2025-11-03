from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Trip, Itinerary
from datetime import datetime
from sqlalchemy.exc import IntegrityError

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('', methods=['POST'])
@jwt_required()
def create_trip():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    if not data or not all(key in data for key in ['name', 'start_date', 'end_date']):
        return jsonify({'message': 'Missing required trip data'}), 400

    try:
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD'}), 400

    if start_date > end_date:
        return jsonify({'message': 'Start date cannot be after end date'}), 400

    new_trip = Trip(
        name=data['name'],
        start_date=start_date,
        end_date=end_date,
        user_id=current_user_id
    )

    try:
        db.session.add(new_trip)
        db.session.commit()

        # Create a default itinerary
        for i in range((new_trip.end_date - new_trip.start_date).days + 1):
            new_itinerary = Itinerary(
                day=i + 1,
                trip_id=new_trip.id
            )
            db.session.add(new_itinerary)
        db.session.commit()

        return jsonify({"message": "Trip created successfully", "trip_id": new_trip.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Database error: Could not create trip'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'An unexpected error occurred: {str(e)}'}), 500

@trips_bp.route('', methods=['GET'])
@jwt_required()
def get_all_trips():
    current_user_id = get_jwt_identity()
    try:
        trips = Trip.query.filter_by(user_id=current_user_id).all()
        output = []
        for trip in trips:
            trip_data = {}
            trip_data['id'] = trip.id
            trip_data['name'] = trip.name
            trip_data['start_date'] = trip.start_date.isoformat()
            trip_data['end_date'] = trip.end_date.isoformat()
            output.append(trip_data)
        return jsonify({'trips': output})
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred: {str(e)}'}), 500

@trips_bp.route('/<int:trip_id>', methods=['GET'])
@jwt_required()
def get_trip(trip_id):
    current_user_id = get_jwt_identity()
    try:
        trip = Trip.query.filter_by(id=trip_id, user_id=current_user_id).first()

        if not trip:
            return jsonify({'message': 'Trip not found or unauthorized'}), 404

        itineraries = Itinerary.query.filter_by(trip_id=trip.id).order_by(Itinerary.day).all()
        itinerary_data = []
        for item in itineraries:
            itinerary_data.append({
                'day': item.day,
                'activities': item.activities
            })

        trip_data = {
            'id': trip.id,
            'name': trip.name,
            'start_date': trip.start_date.isoformat(),
            'end_date': trip.end_date.isoformat(),
            'itinerary': itinerary_data
        }
        return jsonify({'trip': trip_data})
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred: {str(e)}'}), 500

@trips_bp.route('/<int:trip_id>', methods=['PUT'])
@jwt_required()
def update_trip(trip_id):
    data = request.get_json()
    current_user_id = get_jwt_identity()
    try:
        trip = Trip.query.filter_by(id=trip_id, user_id=current_user_id).first()

        if not trip:
            return jsonify({'message': 'Trip not found or unauthorized'}), 404

        if not data:
            return jsonify({'message': 'No data provided for update'}), 400

        if 'name' in data:
            trip.name = data['name']
        if 'start_date' in data:
            try:
                trip.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'message': 'Invalid start_date format. Use YYYY-MM-DD'}), 400
        if 'end_date' in data:
            try:
                trip.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'message': 'Invalid end_date format. Use YYYY-MM-DD'}), 400

        if trip.start_date and trip.end_date and trip.start_date > trip.end_date:
            return jsonify({'message': 'Start date cannot be after end date'}), 400

        db.session.commit()
        return jsonify({'message': 'Trip updated successfully'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Database error: Could not update trip'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'An unexpected error occurred: {str(e)}'}), 500

@trips_bp.route('/<int:trip_id>', methods=['DELETE'])
@jwt_required()
def delete_trip(trip_id):
    current_user_id = get_jwt_identity()
    try:
        trip = Trip.query.filter_by(id=trip_id, user_id=current_user_id).first()

        if not trip:
            return jsonify({'message': 'Trip not found or unauthorized'}), 404

        db.session.delete(trip)
        db.session.commit()
        return jsonify({'message': 'Trip deleted successfully'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Database error: Could not delete trip'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'An unexpected error occurred: {str(e)}'}), 500
