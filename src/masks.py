def get_mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номера банковской карты"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        raise ValueError
    card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
    formatted_card_mask = " ".join(
        card_mask[i : i + 4] for i in range(0, len(card_mask), 4)
    )
    return formatted_card_mask


def get_mask_account(account_number: int) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        raise ValueError
    account_mask = "**" + account_number_str[-4:]
    return account_mask

# использование функции
card_number = int(input())
account_number = int(input())
print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
