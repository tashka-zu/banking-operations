from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(info_account_or_card: str) -> str:
    """Обработка информации о о картах и счетах"""
    if "Счёт" or "Счет" in info_account_or_card:
        account_number = info_account_or_card[-1]
        masked_number = get_mask_account(account_number)
        return info_account_or_card.replace(account_number, masked_number)
    else:
        card_number = info_account_or_card[-1]
        masked_number = get_mask_card_number(card_number)
        return info_account_or_card.replace(card_number, masked_number)

info_account_or_card = str(input())
print(mask_account_card(info_account_or_card))
