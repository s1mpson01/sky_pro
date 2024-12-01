def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX"""

    if len(str(card_number)) == 16 and card_number > 0 and isinstance(card_number, int):
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        raise Exception("Номер карты должен состоять из 16 цифр")


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета (20цифр)
    и возвращает его маску в формате **XXXX"""

    if len(str(account_number)) == 20 and account_number > 0 and isinstance(account_number, int):
        return f"**{str(account_number)[-4:]}"
    else:
        raise Exception("Номер счета должен состоять из 20 цифр")
