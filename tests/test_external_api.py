from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_to_rub():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    assert convert_to_rub(transaction) == 31957.58


@patch("requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 435.649305}

    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    assert convert_to_rub(transaction) == 435.649305
    mock_get.assert_called_once()


@patch("requests.get")
def test_convert_to_rub_error(mock_get):
    mock_get.return_value.status_code = 500

    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    assert convert_to_rub(transaction) is None
    mock_get.assert_called_once()
