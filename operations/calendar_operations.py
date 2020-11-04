from models.calendar_model import Calendar
from models.calendar_model import User


class CalendarOperations:

    def __init__(self):
        pass

    @staticmethod
    def get_calendar(user_uuid):
        selected_user = User.objects(uuid=user_uuid)
        response = Calendar.objects(user__uuid=selected_user.uuid)
        return response

    @staticmethod
    def get_week(user_uuid, selected_weeks):
        min_week = int(selected_weeks.split("_")[0])
        max_week = int(selected_weeks.split("_")[1])
        selected_user = User.objects(uuid=user_uuid)
        response = Calendar.objects(slice__weeks=[min_week, max_week], user__uuid=selected_user.uuid)
        return response

    @staticmethod
    def get_day(user_uuid, week_number, day):
        selected_user = User.objects(uuid=user_uuid)
        response = Calendar.objects(user__uuid=selected_user.uuid, weeks=week_number).only(day)
        return response

    @staticmethod
    def create_calendar(user_uuid, request):
        calendar_info = request.json
        selected_user = User.objects(uuid=user_uuid)
        calendar_obj = {
            'user': selected_user,
            'week': calendar_info['number']
        }
        response = Calendar(**calendar_obj).save()
        return response


    @staticmethod
    def set_day(user_uuid, info):
        selected_user = User.objects(uuid=user_uuid)
        User.objects(selected_user.uuid).update(**info)
        response = Calendar.objects()
        return response
