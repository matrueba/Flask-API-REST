from flask import Blueprint, request, jsonify, make_response
from operations.user_operations import UserOperations


users = Blueprint('users', __name__)
user_op = UserOperations()


@users.route('/raw_users', methods=['GET'])
# This will only accesible for admin
def get_raw_users():
    response = user_op.get_users('uuid', 'account_info')
    return make_response(jsonify(response))


@users.route('/users', methods=['GET'])
def get_users():
    response = user_op.get_users('uuid', 'account_info.mail', 'account_info.username')
    return make_response(jsonify(response))


@users.route('/raw_users/<uuid>', methods=['GET', ])
# This will only accesible for admin
def get_raw_user(uuid):
    response = user_op.get_user('uuid', 'account_info', uuid=uuid)
    return make_response(jsonify(response))


@users.route('/users/<uuid>', methods=['GET', 'PUT', 'DELETE'])
def user_info(uuid):
    if request.method == 'GET':
        response = user_op.get_user('uuid', 'account_info.mail', 'account_info.username', uuid=uuid)
    elif request.method == 'PUT':
        update_data = request.json
        response = user_op.update_user(update_data, uuid=uuid)
    elif request.method == 'DELETE':
        response = user_op.delete_user(uuid=uuid)
    else:
        response = 404
    return make_response(jsonify(response))


@users.route('/users/create', methods=['POST'])
def create_user():
    response = user_op.create_user(request)
    return make_response(jsonify(response))


@users.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404




