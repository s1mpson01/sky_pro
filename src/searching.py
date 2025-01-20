import re
from collections import Counter


def get_information_by_description(my_list: list[dict], string_search: str) -> list[dict]:
    """
    Принимать список словарей с данными о банковских операциях
    и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка.
    """
    result = []
    pattern = re.compile(string_search, re.I)

    for i in my_list:
        string_from_dict = ", ".join(f"{k} {v}" for k, v in i.items())
        result_pattern = pattern.search(string_from_dict)
        if result_pattern:
            result.append(i)
    return result


def get_info_by_category(my_list: list[dict], list_of_category: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    description_list = []
    result_dict = {}

    for i in my_list:
        value_description = i.get("description")
        if value_description in list_of_category:
            description_list.append(value_description)

    result_counted = Counter(description_list)

    for key, value in result_counted.items():
        result_dict[key] = value
    return result_dict
