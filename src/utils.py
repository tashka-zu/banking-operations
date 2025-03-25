import json
import logging
import os

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/utils.log")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def load_transactions(file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if data:
                logger.info(f"Данные успешно загружены из файла {file_path}.")
                return data
            else:
                logger.error(f"Файл {file_path} пуст или не содержит данных.")
                return []
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []


file_path = "../data/operations.json"
transactions = load_transactions(file_path)
