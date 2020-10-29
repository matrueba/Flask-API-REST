from models import User


class ClientOperations:

    @staticmethod
    def get_clients(*fields_to_return):
        response = User.objects.only(*fields_to_return)
        return response

    @staticmethod
    def get_client(*fields_to_return, **filters):
        response = User.objects(**filters).only(*fields_to_return)
        return response

    @staticmethod
    def create_client(update_data, **filters):
        pass

    @staticmethod
    def update_client(update_data, **filters):
        response = User.objects(filters).update(**update_data)
        return response

    def push_measure(self, uuid, measure):
        #measure['bmi'] = self.calculate_bmi(measure)
        #measure['ffmi'] = self.calculate_ffmi(measure)
        response = User.objects(uuid=uuid).update(push__client__measures=measure)
        return response

    @staticmethod
    def get_measure(uuid, date):
        query = {
            'uuid': uuid,
            'client.measures': {'$date': date}
        }

        response = User.objects(uuid=uuid, client__measures__date=date).only('client.measures')
        return response

    @staticmethod
    def update_measure(update_data, **filters):
        response = User.objects(**filters).update(**update_data)
        return response

    @staticmethod
    def delete_measure(uuid, date):
        response = User.objects(uuid=uuid, client__measures__date=date).delete()
        return response

    @staticmethod
    def calculate_ffmi(measure):
        return 1

    @staticmethod
    def calculate_bmi(measure):
        return 1
