import json
import os


def load_transactions(file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if data:
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []
