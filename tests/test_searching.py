from src.searching import get_info_by_category, get_information_by_description

result_var_1 = [
    {
        "id": 4234093.0,
        "state": "EXECUTED",
        "date": "2021-07-08T07:31:21Z",
        "amount": 23182.0,
        "currency_name": "Ruble",
        "currency_code": "RUB",
        "from": "Visa 0773092093872450",
        "to": "Discover 8602781449570491",
        "description": "Перевод с карты на карту",
    }
]
result_var_2 = {"Перевод организации": 2, "Перевод с карты на карту": 17}


def test_get_information_by_description(transaction_list_of_dict_fixture):
    assert get_information_by_description(transaction_list_of_dict_fixture, "RUB") == result_var_1


def test_get_info_by_category(transaction_list_of_dict_fixture):
    assert (
        get_info_by_category(transaction_list_of_dict_fixture, ["Перевод организации", "Перевод с карты на карту"])
        == result_var_2
    )
