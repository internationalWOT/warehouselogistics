from flask_restful import Resource
from webargs.flaskparser import use_args
from ..schemas.schema_warehouse_balance import Deliver
from .utility_functions_balance_calculation import (
    create_response, update_balance)


class Delivery(Resource):

    def get(self):
        return create_response('GET operator ot implemented yet', 200)

    def delete(self):
        return create_response('Delete operator ot implemented yet', 200)

    @use_args(Deliver)
    def patch(self, args):
        return create_response(update_balance(args['balance_number']), 200)

    def post(self):
        return create_response('POST operator ot implemented yet', 200)
