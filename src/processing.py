def filter_by_state(my_list: list, parameter: str = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state.(по умолчанию 'EXECUTED')
    Возвращает новый список словарей, у которых ключ state
    соответствует указанному значению."""

    return [line for line in my_list if line.get("state") == parameter]


def sort_by_date(my_list: list, sort_parameter: bool = True) -> list:
    """Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате (date)."""

    if sort_parameter:
        text_sort = sorted(my_list, key=lambda x: x.get("date"), reverse=True)
    else:
        text_sort = sorted(my_list, key=lambda x: x.get("date"), reverse=False)
    return text_sort
