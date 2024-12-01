import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """Обрабатывает информацию о картах, счетах и возвращает их маску"""

    type_account_list = ["Maestro ", "MasterCard ", "Visa Classic ", "Visa Platinum ", "Visa Gold ", "Счет "]

    type_account = re.sub(r"\d", "", account_card_number)
    number_account = re.sub(r"\D", "", account_card_number)

    if type_account not in type_account_list:
        raise Exception("Некорректно введен счет или номер карты")
    elif type_account in type_account_list[-1]:
        mask_account_card_number = type_account + get_mask_account(int(number_account))
    else:
        mask_account_card_number = type_account + get_mask_card_number(int(number_account))
    return mask_account_card_number


def get_date(data_string: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    data_string_search = re.search(r"^\d{4}-\d{2}-\d{2}\D\d{2}:\d{2}:\d{2}[.]\d{6}$", data_string)

    if isinstance(data_string_search, re.Match):

        if int(data_string[8:10]) in range(1, 32) and int(data_string[5:7]) in range(1, 13) and int(data_string[:4]) > 0:
            return f"{data_string[8:10]}.{data_string[5:7]}.{data_string[:4]}"
        else:
            raise Exception("Неверный день, месяц или год")

    else:
        raise Exception("Неверный формат")
