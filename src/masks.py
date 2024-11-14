def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX"""

    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску в формате **XXXX"""

    mask_account_number = "**" + str(account_number)[-4:]
    return mask_account_number
