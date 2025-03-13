import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(transaction):
    """возвращает сумму транзакции в рублях"""
    currency_code = transaction.get("operationAmount").get("currency").get("code")
    transaction_amount = float(transaction.get("operationAmount").get("amount"))

    if currency_code == "RUB":
        return transaction_amount

    conversion_url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={transaction_amount}"
    )
    headers = {"apikey": api_key}
    response = requests.get(conversion_url, headers=headers)

    if response.status_code == 200:
        conversion_result = response.json()
        return conversion_result["result"]
    else:
        return None
