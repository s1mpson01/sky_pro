def filter_by_state(my_list: list, parameter: str = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state.(по умолчанию 'EXECUTED')
    Возвращает новый список словарей, у которых ключ state
    соответствует указанному значению."""

    if isinstance(my_list, list) and isinstance(parameter, str):
        return [line for line in my_list if line.get("state") == parameter]
    else:
        raise Exception("Некорректный тип данных")


def sort_by_date(my_list: list, is_sort: bool = True) -> list:
    """Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате (date)."""

    if isinstance(my_list, list) and isinstance(is_sort, bool):
        result = sorted(my_list, key=lambda x: x.get("date"), reverse=is_sort)
        return result
    else:
        raise Exception("Некорректный тип данных")

print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED"))