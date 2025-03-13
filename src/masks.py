def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты"""
    card_number_str = str(card_number)
    if card_number_str == "":
        return ""
    if not card_number_str.isdigit():
        return "Некорректный ввод данных"
    else:
        card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
        formatted_card_mask = " ".join(card_mask[i : i + 4] for i in range(0, len(card_mask), 4))
        return formatted_card_mask


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_number_str = str(account_number)
    if account_number_str == "":
        return ""
    if not account_number_str.isdigit():
        return "Некорректный ввод данных"
    else:
        account_mask = "**" + account_number_str[-4:]
        return account_mask
