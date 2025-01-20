import json

# import logging
from json import JSONDecodeError

# logger = logging.getLogger("utils")
# file_handler = logging.FileHandler("../logs/utils.log", "w")
# file_formater = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s:line-%(lineno)d")
# file_handler.setFormatter(file_formater)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)


def get_list_of_transactions(path: str) -> list:
    """
    Принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    """
    # logger.info("Initialization")
    result = []
    try:
        with open(path) as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                # logger.error("JSONDecodeError")
                return result
    except FileNotFoundError:
        # logger.error("FileNotFound")
        return result
    else:
        # logger.info("Finish")
        return [i for i in data]


# print(get_list_of_transactions("../data/operations.json"))
