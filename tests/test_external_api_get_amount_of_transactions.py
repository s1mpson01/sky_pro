from unittest.mock import patch

import pytest

from src.external_api import get_amount_of_transactions


def test_get_amount_of_transactions_with_rub():
    transaction_rub = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    result = get_amount_of_transactions(transaction_rub)
    assert result == 31957.58


@patch("requests.get")
def test_get_amount_of_transactions_with_usd(mock_request_get):
    transaction_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_request_get.return_value.status_code = 200
    mock_request_get.return_value.json.return_value = {"base": "USD", "data": "2020-07-09", "rates": {"RUB": 70}}
    result = get_amount_of_transactions(transaction_usd)
    assert result == 7000.0


@patch("requests.get", side_effect=Exception("Проблема с сетью"))
def test_get_amount_of_transactions_bad_status(mock_request_get):
    transaction_usd1 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    with pytest.raises(Exception, match="Проблема с сетью"):
        get_amount_of_transactions(transaction_usd1)
