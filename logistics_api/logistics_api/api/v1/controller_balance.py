from flask_restful import Resource
from .utility_functions_balance_calculation import (
    create_response, get_balance)


class Balance(Resource):

    def get(self):
        return create_response(get_balance(), 200)

    def delete(self):
        return create_response('DELETE operator ot implemented yet', 200)

    def patch(self):
        return create_response('PATCH operator ot implemented yet', 200)

    def post(self):
        return create_response('POST operator ot implemented yet', 200)
