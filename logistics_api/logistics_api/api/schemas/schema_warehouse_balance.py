from marshmallow import Schema, fields
from marshmallow.decorators import post_load, validates_schema
from marshmallow import ValidationError


# I want to validate as much of my input as possible in order to get clean data in the application.

class Deliver(Schema):
    balance_number = fields.Integer(required=True)

    @validates_schema
    def validate_balance_number(self, data, **kwargs):
        if not data['balance_number'] >= 0:
            raise ValidationError('Value of field balance_number must be greater than 0')


class Sales(Schema):
    balance_number = fields.Integer(required=True)

    @post_load()
    def convert_balance_number_to_negative(self, data, **kwargs):
        data['balance_number'] = -abs(int(data['balance_number']))
        return data
