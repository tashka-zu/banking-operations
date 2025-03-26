from unittest.mock import patch, mock_open
from src.main import main, load_transactions, filter_transactions_by_status, sort_transactions_by_date, filter_ruble_transactions

# Пример данных для тестирования
transactions_data = [
    {'date': '2021-01-01', 'description': 'Перевод на карту', 'status': 'EXECUTED', 'from': 'Счет 1234', 'to': 'Счет 5678', 'amount': '1000 руб'},
    {'date': '2021-02-01', 'description': 'Оплата счета', 'status': 'CANCELED', 'from': 'Счет 1234', 'to': 'Счет 5678', 'amount': '200 USD'},
    {'date': '2021-03-01', 'description': 'Перевод организации', 'status': 'PENDING', 'from': 'Счет 1234', 'to': 'Счет 5678', 'amount': '300 руб'}
]

def test_load_transactions():
    with patch('builtins.open', mock_open(read_data="[]")):
        result = load_transactions('fake_path.json')
        assert result == []

def test_filter_transactions_by_status():
    result = filter_transactions_by_status(transactions_data, 'EXECUTED')
    assert len(result) == 1
    assert result[0]['status'] == 'EXECUTED'

def test_sort_transactions_by_date():
    result = sort_transactions_by_date(transactions_data, ascending=True)
    assert result[0]['date'] == '2021-01-01'

def test_filter_ruble_transactions():
    result = filter_ruble_transactions(transactions_data)
    assert len(result) == 2

@patch('builtins.input', side_effect=['3', 'EXECUTED', 'да', 'по возрастанию', 'да', 'Перевод', 'нет'])
@patch('builtins.print')
def test_main(mock_print, mock_input):
    with patch('src.main.load_transactions', return_value=transactions_data):
        main()
        mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
