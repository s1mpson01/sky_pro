def filter_by_state(my_list, parameter="EXECUTED"):
    """Принимает список словарей и значение для ключа state.
    Возвращает новый список словарей, у которых ключ state
    соответствует указанному значению."""

    return [line for line in my_list if line.get("state") == parameter]
