from models import User
from werkzeug.security import generate_password_hash
from uuid import uuid4


class UserOperations:

    @staticmethod
    def get_users(*fields_to_return):
        response = User.objects.only(*fields_to_return)
        return response

    @staticmethod
    def get_user(*fields_to_return, **filters):
        response = User.objects(**filters).only(*fields_to_return)
        return response

    @staticmethod
    def create_user(request):
        user_info = request.json
        hashed_pass = generate_password_hash(user_info["password"])
        uuid_gen = uuid4()
        user_obj = {
            'uuid': uuid_gen,
            'account_info': {
                'mail': user_info["mail"],
                'password': hashed_pass,
                'username': user_info["username"]
            }
        }
        user = User(**user_obj).save()
        if user:
            response = {
                'username': user.account_info.username,
                'mail': user.account_info.mail,
                'uuid': user.uuid,
            }
        else:
            response = 404
        return response

    @staticmethod
    def update_user(update_data, **filters):
        response = User.objects(**filters).update(**update_data)
        return response

    @staticmethod
    def delete_user(**filters):
        response = User.objects(**filters).delete()
        return response

