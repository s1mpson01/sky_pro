import json
from json import JSONDecodeError


def get_list_of_transactions(path: str) -> list:
    """
    Принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    """
    result = []
    try:
        with open(path) as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                return result
    except FileNotFoundError:
        return result
    else:
        return [i for i in data]
print(get_list_of_transactions("12"))