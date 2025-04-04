import os

from src.transaction_reader import read_csv, read_excel


def test_read_csv():
    file_path = os.path.join(os.path.dirname(__file__), "../data/transactions.csv")
    result = read_csv(file_path)
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)
    print("test_read_csv passed")


def test_read_excel():
    file_path = os.path.join(os.path.dirname(__file__), "../data/transactions_excel.xlsx")
    result = read_excel(file_path)
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)
    print("test_read_excel passed")
