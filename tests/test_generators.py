from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268

    eur_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]["id"] == 845372817

    jpy_transactions = list(filter_by_currency(transactions, "JPY"))
    assert len(jpy_transactions) == 0


def test_filter_by_currency_empty():
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_transaction_descriptions_multiple(transactions):
    descriptions = transaction_descriptions(transactions)
    assert list(descriptions) == ["Перевод организации", "Перевод со счета на счет", "Перевод в евро"]


def test_transaction_descriptions_single():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    descriptions = transaction_descriptions(transactions)
    assert list(descriptions) == ["Перевод организации"]


def test_transaction_descriptions_empty():
    transactions = []
    descriptions = transaction_descriptions(transactions)
    assert list(descriptions) == []


def test_card_number_generator(card_number_params):
    start, end, expected_numbers = card_number_params
    generator = card_number_generator(start, end)
    generated_numbers = list(generator)
    assert generated_numbers == expected_numbers
