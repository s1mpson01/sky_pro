import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("account_card_number, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Счет 73654108430135874305", "Счет **4305")
                          ])
def test_mask_account_card_with_parametrize(account_card_number, expected):
    assert mask_account_card(account_card_number) == expected


def test_mask_account_card_with_fixture(account_mask):
    assert mask_account_card("Счет 73654108430135874305") == account_mask


def test_mask_account_card_incorrect():
    with pytest.raises(Exception):
        assert mask_account_card("Visa 8990922113665229 Platinum")


def test_mask_account_card_translit():
    with pytest.raises(Exception):
        assert mask_account_card("МастерКард 2999414222426353")


def test_mask_account_card_empty():
    with pytest.raises(Exception):
        assert mask_account_card("")


@pytest.mark.parametrize("data_string, expected",
                         [("2024-03-11T02:55:33.324407", "11.03.2024"),
                          ("2020-01-01T02:26:24.644407", "01.01.2020"),
                          ("2020-04-01T03:26:45.671407", "01.04.2020")
                          ])
def test_get_date_with_parametrize(data_string, expected):
    assert get_date(data_string) == expected


def test_get_date_with_fixture(data_string_fixture):
    assert get_date(data_string_fixture) == "11.03.1999"


def test_get_date_exam_isinstance():
     with pytest.raises(Exception):
         get_date("2022001-01T02:26:24.644407")


def test_get_date_with_incorrect_day():
    with pytest.raises(Exception):
        get_date("2022-01-40T02:26:24.644407")


def test_get_date_with_empty():
    with pytest.raises(Exception):
        get_date("")