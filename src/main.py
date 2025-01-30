from src.processing import filter_by_state, sort_by_date
from src.reading import get_transactions_from_csv, get_transactions_from_excel
from src.searching import get_information_by_description
from src.utils import get_list_of_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Cвязывает функциональности между собой.
    Есть выбор чтения файла json, csv, xlsx.
    Есть сортировка по статусу, по дате, рублевым транзакциям
    и по ключевому слову.
    """

    my_dict = {
        "make_date_filter": False,
        "sort_filter": "",
        "filter_ruble": False,
        "filter_by_input": False,
        "word_by_filter": "",
    }

    print("Привет! Добро пожаловать в программу работы\n" "с банковскими транзакциями.")

    result_read_file = []
    file_selection_input = ""

    while True:
        if file_selection_input not in ["1", "2", "3"]:
            print(
                "Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла"
            )
            file_selection_input = input()
        else:
            break

    if file_selection_input == "1":
        result_read_file = get_list_of_transactions("../data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif file_selection_input == "2":
        result_read_file = get_transactions_from_csv("../data/transactions.csv")
        print("Для обработки выбран CSV-файл")
    elif file_selection_input == "3":
        result_read_file = get_transactions_from_excel("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    transaction_status_input = input()

    while True:
        if transaction_status_input.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {transaction_status_input} недоступен")
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            transaction_status_input = input()
        else:
            result_with_status = filter_by_state(result_read_file, transaction_status_input.upper())
            break

    make_date_filter_input = ""

    while True:
        if make_date_filter_input.upper() not in ["ДА", "НЕТ"]:
            print("Отсортировать операции по дате? Да/Нет")
            make_date_filter_input = input()
        else:
            break

    if make_date_filter_input.upper() == "ДА":
        my_dict["make_date_filter"] = True

        print("Отсортировать по возрастанию или по убыванию?")
        sort_date_input = input()

        while True:
            if sort_date_input.upper() not in ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"]:
                print("Отсортировать по возрастанию или по убыванию?")
                sort_date_input = input()
            else:
                break

        if sort_date_input.upper() == "ПО УБЫВАНИЮ":
            my_dict["sort_filter"] = "ПО УБЫВАНИЮ"
        elif sort_date_input.upper() == "ПО ВОЗРАСТАНИЮ":
            my_dict["sort_filter"] = "ПО ВОЗРАСТАНИЮ"

    filter_ruble_input = ""

    while True:
        if filter_ruble_input.upper() not in ["ДА", "НЕТ"]:
            print("Выводить только рублевые транзакции? Да/Нет")
            filter_ruble_input = input()
        else:
            break

    if filter_ruble_input.upper() == "ДА":
        my_dict["filter_ruble"] = True

    filter_by_input = ""
    word_by_filter = ""

    while True:
        if filter_by_input.upper() not in ["ДА", "НЕТ"]:
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            filter_by_input = input()
        else:
            break

    if filter_by_input.upper() == "ДА":
        my_dict["filter_by_input"] = True
        print("Введите слово")
        word_by_filter = input()
        my_dict["word_by_filter"] = word_by_filter

    if my_dict["make_date_filter"]:
        if my_dict["sort_filter"] == "ПО УБЫВАНИЮ":
            result_by_sort = sort_by_date(result_with_status)
        else:
            result_by_sort = sort_by_date(result_with_status, True)
    else:
        result_by_sort = result_with_status

    if my_dict["filter_ruble"]:
        result_by_ruble = get_information_by_description(result_by_sort, "RUB")
    else:
        result_by_ruble = result_by_sort

    if my_dict["filter_ruble"]:
        result_by_word = get_information_by_description(result_by_ruble, word_by_filter)
    else:
        result_by_word = result_by_ruble

    if len(result_by_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(result_by_word)}")

        for i in result_by_word:
            data_field = get_date(i["date"])
            description_field = i["description"]
            to_field = mask_account_card(i["to"])

            if file_selection_input != "1":
                if i["from"] is None:
                    print(
                        f"{data_field} {description_field}\n"
                        f"{to_field}\n"
                        f"Сумма: {i["amount"]} {i["currency_code"]}\n"
                    )
                else:
                    from_field = mask_account_card(i["from"])
                    print(
                        f"{data_field} {description_field}\n"
                        f"{from_field} -> {to_field}\n"
                        f"Сумма: {i["amount"]} {i["currency_code"]}\n"
                    )

            else:
                if i.get("from", None) is None:
                    print(
                        f"{data_field} {description_field}\n"
                        f"{to_field}\n"
                        f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["code"]}\n"
                    )
                else:
                    from_field = mask_account_card(i["from"])
                    print(
                        f"{data_field} {description_field}\n"
                        f"{from_field} -> {to_field}\n"
                        f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["code"]}\n"
                    )
