import pandas as pd


def read_csv(file_path):
    """Функция, которая считывает финансовые транзакции из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel(file_path):
    """Функция, которая считывает финансовые транзакции из файла Excel."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
