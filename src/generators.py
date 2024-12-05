def filter_by_currency(my_list: list, currency: str):
    """
    Принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """

    return (i for i in my_list if i.get("operationAmount").get("currency").get("code") == currency)


def transaction_descriptions(my_list: list):
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    return (i.get("description") for i in my_list)


def card_number_generator(start_number: int, end_number: int):
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """

    number = ("0" * (16 - len(str(i))) + str(i) for i in range(start_number, end_number))
    map_result = map(lambda x: f"{x[0:4]} {x[4:8]} {x[8:12]} {x[12:16]}", number)

    return map_result
