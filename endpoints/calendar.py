from flask import Blueprint, request, jsonify, make_response
from operations.calendar_operations import CalendarOperations

calendar = Blueprint('calendar', __name__)
calendar_op = CalendarOperations()


@calendar.route('/calendar/<uuid>', methods=['GET', 'POST'])
def get_calendar(uuid):
    response = calendar_op.get_calendar(user_uuid=uuid)
    return make_response(jsonify(response))


@calendar.route('/calendar/week/<uuid>/<selected_weeks>', methods=['GET', 'POST'])
def get_week(uuid, selected_weeks):
    response = calendar_op.get_week(uuid=uuid, selected_weeks=selected_weeks)
    return make_response(jsonify(response))

@calendar.route('/calendar/<week>/<day>/<uuid>', methods=['GET', 'POST'])
def get_day(uuid, day, week):
    if request.method == 'GET':
        response = calendar_op.get_day(uuid, week, day)
    elif request.method == 'POST':
        info = request.json
        response = calendar_op.set_day(uuid, day, week, info)
    else:
        response = 404
    return make_response(jsonify(response))


@calendar.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

