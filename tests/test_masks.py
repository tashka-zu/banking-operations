from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number[0]) == "1234 56** **** 7890"
    assert get_mask_card_number(card_number[1]) == "5721 96** **** 0987"
    assert get_mask_card_number(card_number[2]) == "3956 04** **** 9843"
    assert get_mask_card_number(card_number[3]) == "1945 87** **** 0165"
    assert get_mask_card_number(card_number[4]) == "Некорректный ввод данных"


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == ""


def test_get_mask_account(account_number):
    assert get_mask_account(account_number[0]) == "**6503"
    assert get_mask_account(account_number[1]) == "**9365"
    assert get_mask_account(account_number[2]) == "**9265"
    assert get_mask_account(account_number[3]) == "**5820"
    assert get_mask_account(account_number[4]) == "Некорректный ввод данных"


def test_get_mask_account_empty():
    assert get_mask_account("") == ""
