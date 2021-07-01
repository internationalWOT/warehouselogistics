from flask import json, Response, abort


# This is ugly but in accordance to the instructions.
# This is instead of me creating a database and working with models instead
data = {'total_balance':  0}


def update_balance(balance_number):
    if not __valid__calculated_balance(balance_number):
        msg = {
            'Message': (
                f'Balance can not be negative. '
                f'Current balance is still {data["total_balance"]}')}
        abort(create_response(msg, 500))
    data['total_balance'] = data['total_balance'] + balance_number
    return data


def get_balance():
    return data


def create_response(msg, status_code, mimetype='application/json'):
    return Response(json.dumps(msg), status=status_code, mimetype=mimetype)


def __valid__calculated_balance(balance_number):
    return True if data['total_balance'] + balance_number >= 0 else False
