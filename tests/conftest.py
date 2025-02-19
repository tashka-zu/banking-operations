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


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 845372817,
            "state": "EXECUTED",
            "date": "2020-01-01T10:00:00.000000",
            "operationAmount": {"amount": "10000.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод в евро",
            "from": "Счет 11111111111111111111",
            "to": "Счет 22222222222222222222",
        },
    ]


@pytest.fixture(
    params=[
        (1, 1, ["0000000000000001"]),
        (2, 4, ["0000000000000002", "0000000000000003", "0000000000000004"]),
        (5, 5, ["0000000000000005"]),
        (9999999999999999, 9999999999999999, ["9999999999999999"]),
    ]
)
def card_number_params(request):
    return request.param
