from flask import jsonify, Blueprint, request
from app.services.apartment_service import ApartmentService
from app.mapping.apartment_schema import ApartmentSchema
from app.dto import ResponseBuilder
from app.validators import validate_with, validate_exists

apartment = Blueprint('apartment', __name__)

ps = ApartmentSchema(many=True)
apartment_schema = ApartmentSchema()
apartment_service = ApartmentService()
response = ResponseBuilder()

@apartment.route('/', methods=['GET'])
def index():
    response.add_status_code(200).add_message('This is apartment resource!').add_data()
    return jsonify(response.build()), response.status_code


@apartment.route('/create', methods=['POST'])
@validate_with(ApartmentSchema)
def create(validated_data):
    apartment = validated_data
    response.add_status_code(200).add_message('Apartment created!').add_data(
        {"apartment created": apartment_schema.dump(apartment_service.create(apartment))}
    )
    return jsonify(response.build()), response.status_code


@apartment.route('/update/<int:id>', methods=['PUT'])
@validate_with(ApartmentSchema)
@validate_exists(apartment_service, response)
def update(validated_data, id):
    apartment = validated_data
    response.add_status_code(200).add_message('Apartment updated!').add_data(
        {"apartment updated": apartment_schema.dump(apartment_service.update(apartment, id))}
    )
    return jsonify(response.build()), response.status_code


@apartment.route('/findbyid/<int:id>', methods=['GET'])
@validate_exists(apartment_service, response)
def find_by_id(id):
    response.add_status_code(200).add_message('Apartment found!').add_data({"apartment": apartment_schema.dump(apartment_service.find_by_id(id))})
    return jsonify(response.build()), response.status_code
    
    
@apartment.route('/findall', methods=['GET'])
def find_all():
    if not apartment_service.find_all():
        response.add_status_code(400).add_message('There are no departments created!').add_data()
        return jsonify(response.build()), response.status_code
    response.add_status_code(200).add_message('Apartments found!').add_data({"apartments": ps.dump(apartment_service.find_all())})
    return jsonify(response.build()), response.status_code



@apartment.route('/delete/<int:id>', methods=['DELETE'])
@validate_exists(apartment_service, response)
def delete(id):
    response.add_status_code(200).add_message('Apartment deleted!').add_data({"apartment deleted": apartment_schema.dump(apartment_service.delete(id))})
    return jsonify(response.build()), response.status_code

    
@apartment.route('/search', methods=['GET'])
def search():
    lease_min = request.args.get('lease_min')
    lease_max = request.args.get('lease_max')
    response.add_status_code(200).add_message('Apartment found!').add_data({"apartments": ps.dump(apartment_service.search(lease_min, lease_max))})
    return jsonify(response.build()), response.status_code
  