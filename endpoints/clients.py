from flask import Blueprint, request, jsonify, make_response
from models import User
from operations.client_operations import ClientOperations

clients = Blueprint('clients', __name__)
client_op = ClientOperations()


@clients.route('/clients', methods=['GET'])
def get_clients():
    response = client_op.get_clients('uuid', 'client')
    return make_response(jsonify(response))


@clients.route('/clients/<uuid>', methods=['GET', 'PUT', 'DELETE'])
def client_info(uuid):
    response = client_op.get_client('uuid', 'client', uuid=uuid)
    return make_response(jsonify(response))


@clients.route('/clients/<uuid>/create', methods=['POST'])
def create_client(uuid):
    client_info = request.json
    response = client_op.create_client(client_info, uuid=uuid)
    return make_response(jsonify(response))


@clients.route('/clients/<uuid>/measure', methods=['GET', 'POST', 'PUT', 'DELETE'])
def measure_info(uuid):
    if request.method == 'GET':
        response = client_op.get_measure(uuid, request.json['date'])
    elif request.method == 'POST':
        measure = request.json
        response = client_op.push_measure(uuid, measure)
    elif request.method == 'PUT':
        response = client_op.update_measure(request.json, uuid=uuid)
    elif request.method == 'DELETE':
        response = client_op.delete_measure(uuid, request.json['date'], )
    else:
        response = 404
    return make_response(jsonify(response))


@clients.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

