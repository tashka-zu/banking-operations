from datetime import datetime


def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: list, descending: bool = True) -> list:
    """Сортирует список словарей по значению ключа 'date'"""
    operations_with_datetime = [
        {**operation, 'date': datetime.fromisoformat(operation['date'])}
        for operation in operations
    ]

    # Сортируем список по ключу 'date'
    sorted_operations = sorted(
        operations_with_datetime,
        key=lambda x: x['date'],
        reverse=descending
    )

    # Преобразуем объекты datetime обратно в строки
    sorted_operations_with_str_date = [
        {**operation, 'date': operation['date'].isoformat()}
        for operation in sorted_operations
    ]

    return sorted_operations_with_str_date
