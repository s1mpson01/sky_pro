def filter_by_currency(my_list, currency):
    """
    Принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """
    result = (i for i in my_list if i.get("operationAmount").get("currency").get("code")
              == currency)

    return result
