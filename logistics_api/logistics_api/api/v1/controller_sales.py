from flask_restful import Resource
from webargs.flaskparser import use_args
from ..schemas.schema_warehouse_balance import Sales
from .utility_functions_balance_calculation import (
    create_response, update_balance)

class Sales(Resource):

    def get(self):
        return create_response('GET operator ot implemented yet', 200)

    def delete(self):
        return create_response('DELETE operator ot implemented yet', 200)

    @use_args(Sales)
    def patch(self, args):
        return create_response(update_balance(args['balance_number']), 200)

    def post(self, args):
        return create_response('POST operator ot implemented yet', 200)


