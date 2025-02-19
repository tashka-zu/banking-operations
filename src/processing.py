from datetime import datetime


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(lst: list, reverse_state: bool = False) -> list:
    """Сортирует список словарей по значению ключа 'date'"""

    def get_date(dictionary: dict) -> datetime:
        """Преобразует строку даты из словаря в объект datetime"""
        return datetime.strptime(dictionary["date"], "%Y-%m-%dT%H:%M:%S.%f")

    new_lst = sorted(lst, key=get_date, reverse=not reverse_state)
    return new_lst
