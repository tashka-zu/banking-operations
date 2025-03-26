import csv
import json
import os

import pandas as pd

from src.utils import search_transactions_by_description


def load_transactions(file_path):
    """Загружаем транзакции из файла"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    absolute_path = os.path.abspath(os.path.join(base_dir, file_path))

    if file_path.endswith(".json"):
        with open(absolute_path, "r") as file:
            return json.load(file)
    elif file_path.endswith(".csv"):
        with open(absolute_path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(absolute_path).to_dict(orient="records")
    else:
        raise ValueError("Неподдерживаемый формат файла")


def filter_transactions_by_status(transactions, status):
    """Фильтруем транзакции по статусу"""
    return [transaction for transaction in transactions if transaction.get("status", "").upper() == status.upper()]


def sort_transactions_by_date(transactions, ascending=True):
    """Сортируем транзакции по дате"""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_ruble_transactions(transactions):
    """Фильтруем транзакции, где транзакции только в рублях."""
    return [transaction for transaction in transactions if "руб" in transaction.get("amount", "")]


def main():
    """Основная функция программы для работы с банковскими транзакциями"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта меню: ")
    file_paths = {"1": "data/transactions.json", "2": "data/transactions.csv", "3": "data/transactions_excel.xlsx"}

    if choice in file_paths:
        file_path = file_paths[choice]
        print(f"Для обработки выбран {file_path}.")
        transactions = load_transactions(file_path)

        status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:"""
        ).strip()
        while status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{status}" недоступен.')
            status = input(
                """Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:"""
            ).strip()

        transactions = filter_transactions_by_status(transactions, status)
        print(f'Операции отфильтрованы по статусу "{status}"')

        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == "да":
            order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            transactions = sort_transactions_by_date(transactions, ascending=order == "по возрастанию")

        ruble_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if ruble_choice == "да":
            transactions = filter_ruble_transactions(transactions)

        search_choice = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
        )
        if search_choice == "да":
            search_string = input("Введите слово для поиска: ").strip()
            transactions = search_transactions_by_description(transactions, search_string)

        if transactions:
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(transactions)}")
            for transaction in transactions:
                print(f"{transaction['date']} {transaction['description']}")
                print(f"{transaction['from']} -> {transaction['to']}")
                print(f"Сумма: {transaction['amount']}")
                print()
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Неверный выбор. Пожалуйста, выберите доступный пункт меню.")


if __name__ == "__main__":
    main()
