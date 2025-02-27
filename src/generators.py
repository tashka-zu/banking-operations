from typing import Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Функция возвращает итератор,
    который поочередно выдает транзакции,
    где валюта операции соответствует заданной
    """
    return (
        transaction
        for transaction in transactions
        if transaction["operationAmount"]["currency"]["code"] == currency_code
    )


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Функция, которая принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        yield f"{number:016}"
