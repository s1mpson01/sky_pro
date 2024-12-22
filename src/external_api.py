import os

import requests
from dotenv import load_dotenv


def get_amount_of_transactions(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amounts = float(transaction["operationAmount"]["amount"])

    if currency == "RUB":
        return amounts
    else:
        load_dotenv()
        apilayer_key = os.getenv("APILAYER_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": apilayer_key}
        try:
            response = requests.get(url, headers=headers)
            status_code = response.status_code
        except Exception:
            raise Exception("Проблема с сетью")
        else:
            if status_code == 200:
                result = response.json()
                course_price = result["rates"]["RUB"]
                total_cost = round(float(course_price) * amounts, 2)
                return total_cost
            else:
                raise Exception(response.reason)
