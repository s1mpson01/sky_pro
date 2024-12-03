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
