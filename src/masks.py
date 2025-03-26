import logging
import os

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"))
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты"""
    card_number_str = str(card_number)
    if card_number_str == "":
        logger.error("Пустой ввод данных для номера карты")
        return ""
    if not card_number_str.isdigit():
        logger.error("Некорректный ввод данных для номера карты")
        return "Некорректный ввод данных"
    else:
        card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
        formatted_card_mask = " ".join(card_mask[i : i + 4] for i in range(0, len(card_mask), 4))
        logger.info(f"Номер карты успешно замаскирован: {formatted_card_mask}")
        return formatted_card_mask


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_number_str = str(account_number)
    if account_number_str == "":
        logger.error("Пустой ввод данных для номера счета")
        return ""
    if not account_number_str.isdigit():
        logger.error("Некорректный ввод данных для номера счета")
        return "Некорректный ввод данных"
    else:
        account_mask = "**" + account_number_str[-4:]
        logger.info(f"Номер счета успешно замаскирован: {account_mask}")
        return account_mask


get_mask_card_number("1234567890123456")
get_mask_account("1234567890")
