import pytest


@pytest.fixture
def card_number():
    return [1234566503867890, 5721964654130987, 3956046466729843, 19458757634530165, "mwmw"]


@pytest.fixture
def account_number():
    return [76590452896063616503, 51243646541345349365, 54312364667234529265, 12463357634534555820, "mwmw"]


@pytest.fixture
def cards_and_accounts():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def dates():
    return ["2024-03-11T02:26:18.671407", "2000-01-01T00:00:00.000000", "1999-12-31T23:59:59.999999", "mwmw"]


@pytest.fixture
def list_of_dictionaries():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
