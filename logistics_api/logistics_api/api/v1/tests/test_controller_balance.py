from logistics_api.api.v1.utility_functions_balance_calculation import (
    __valid__calculated_balance,
    get_balance,
    update_balance,
)
import pytest


def test_if_balance_is_valid():
    assert __valid__calculated_balance(1) is True
    assert __valid__calculated_balance(-1) is False


def test_if_balance_is_returned(data):
    assert get_balance()['total_balance'] == 0


def test_if_balance_updates(data):
    assert data['total_balance'] == 0
    data2 = update_balance(1)
    assert data2['total_balance'] == 1


@pytest.fixture
def data():
    return {'total_balance':  0}
