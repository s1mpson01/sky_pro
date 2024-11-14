import re
from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card_number: str) -> str:
    """Обрабатывает информацию о картах, счетах и возвращает их маску"""

    type_account = re.sub(r"\d","", account_card_number)
    number_account = re.sub(r"\D", "",account_card_number)
    match = re.search("Счет", account_card_number)

    if match:
        mask_account_card_number = type_account + get_mask_account(int(number_account))
    else:
        mask_account_card_number = type_account + get_mask_card_number(int(number_account))

    return mask_account_card_number


def get_date(data_string: str) -> str:
    """Возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    return f"{str(data_string[8:10])}.{str(data_string[5:7])}.{str(data_string[:4])}"
