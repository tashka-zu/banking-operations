import json
from unittest.mock import mock_open, patch

from src.utils import count_transactions_by_category, load_transactions, search_transactions_by_description


def test_load_transaction():
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", '
        '"date": "2019-08-26T10:50:58.294041", '
        '"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, '
        '"description": "Перевод организации", "from": "Maestro 1596837868705199", '
        '"to": "Счет 64686473678894779589"}]'
    )
    mock_file = mock_open(read_data=mock_data)
    with patch("builtins.open", mock_file):
        with patch("os.path.exists", return_value=True):
            outcome = load_transactions("../data/operations.json")

    expected_outcome = json.loads(mock_data)
    assert outcome == expected_outcome
    mock_file.assert_called_once()


def test_load_transaction_error():
    mock_error = mock_open()
    mock_error.side_effect = FileNotFoundError("File not found")
    with patch("builtins.open", mock_error):
        with patch("os.path.exists", return_value=True):
            outcome = load_transactions("non_existent.json")

    assert outcome == []
    mock_error.assert_called_once()


def test_search_transactions_by_description():
    transactions = [
        {"description": "Перевод на карту"},
        {"description": "Оплата счета"},
        {"description": "Перевод организации"},
    ]
    assert len(search_transactions_by_description(transactions, "Перевод")) == 2
    assert len(search_transactions_by_description(transactions, "Счет")) == 1
    assert len(search_transactions_by_description(transactions, "Несуществующий")) == 0


def test_count_transactions_by_category():
    transactions = [
        {"description": "Перевод на карту"},
        {"description": "Оплата счета"},
        {"description": "Перевод организации"},
    ]
    categories = ["Перевод", "Оплата"]
    result = count_transactions_by_category(transactions, categories)
    assert result == {"Перевод": 2, "Оплата": 1}
