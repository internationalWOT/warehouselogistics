from flask import Blueprint
from flask_restful import Api
from logistics_api.api.v1.controller_balance import (
    Balance)
from logistics_api.api.v1.controller_deliver import (
    Delivery)

from logistics_api.api.v1.controller_sales import (
    Sales)

import webargs

api_bp_v1 = Blueprint('api_1', __name__, url_prefix="/api/v1")
api_v1 = Api(api_bp_v1)

api_v1.add_resource(Balance, '/balance')
api_v1.add_resource(Sales, '/sales')
api_v1.add_resource(Delivery, '/delivery')

# this should be moved and cleaned up to its own error handler in the future.
@webargs.flaskparser.parser.error_handler
def webargs_validation_handler(
        error, req, schema, *, error_status_code, error_headers):
    """Handles errors during parsing. Aborts the current HTTP request and
    responds with a 422 error.
    """
    status_code = error_status_code or webargs.core.DEFAULT_VALIDATION_STATUS
    webargs.flaskparser.abort(
        status_code,
        exc=error,
        messages=error.messages,
    )