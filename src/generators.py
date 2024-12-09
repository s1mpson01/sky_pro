from typing import Iterator


def filter_by_currency(my_list: list, currency: str) -> Iterator:
    """
    Принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """
    if isinstance(my_list, list) and isinstance(currency, str):
        return (i for i in my_list if i.get("operationAmount").get("currency").get("code") == currency)
    else:
        raise Exception("Некорректные входные данные")


def transaction_descriptions(my_list: list) -> Iterator:
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    result = (i.get("description") for i in my_list)
    for x in result:
        yield x


def card_number_generator(start_number: int, end_number: int) -> Iterator:
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """

    if not (isinstance(start_number, int) and isinstance(end_number, int)):
        raise Exception("Начало и конец должны быть целыми числами")
    elif start_number >= end_number:
        raise Exception("Конец диапазона не может быть больше начала")
    elif (start_number or end_number) <= 0:
        raise Exception("Границы диапазона должны быть положительные числа")
    elif (start_number or end_number) > 10000000000000000:
        raise Exception("Максимальное число для диапазона 10000000000000")
    else:
        number = ("0" * (16 - len(str(i))) + str(i) for i in range(start_number, end_number))
        map_result = map(lambda x: f"{x[0:4]} {x[4:8]} {x[8:12]} {x[12:16]}", number)

    return map_result
