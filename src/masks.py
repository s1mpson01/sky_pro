# import logging
#
# logger = logging.getLogger("masks")
# file_handler = logging.FileHandler("../logs/masks.log", "w")
# file_formater = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s:line-%(lineno)d")
# file_handler.setFormatter(file_formater)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX"""
    # logger.info("Initialization")
    if len(str(card_number)) == 16:
        # logger.info("Finish")
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        # logger.critical(f"{card_number} не из 16 цифр")
        raise Exception("Номер карты должен состоять из 16 цифр")


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета (20цифр)
    и возвращает его маску в формате **XXXX"""
    # logger.info("Initialization")
    if len(str(account_number)) == 20:
        # logger.info("Finish")
        return f"**{str(account_number)[-4:]}"
    else:
        # logger.critical("Номер счета должен состоять из 20 цифр")
        raise Exception("Номер счета должен состоять из 20 цифр")
