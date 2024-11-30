from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_15_symbols():
    with pytest.raises(Exception):
        get_mask_card_number(111122223333444)


def test_get_mask_card_number_17_symbols():
    with pytest.raises(Exception):
        get_mask_card_number(11112222333344445)


def test_get_mask_card_number_empty():
    with pytest.raises(Exception):
        get_mask_card_number(None)


def test_get_mask_card_number_negative_14_symbols():
    with pytest.raises(Exception):
        get_mask_card_number(-111122223333444)


@pytest.mark.parametrize("card_number, expected", [(1111222233334444, "1111 22** **** 4444"),
                                                   (4444555566667777, "4444 55** **** 7777"),
                                                   (1234567812345678, "1234 56** **** 5678")])
def test_get_mask_card_number_with_parametrize(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_with_fixture(card_of_number):
    assert get_mask_card_number(9999888877776666) == card_of_number


def test_get_mask_account_19_symbols():
    with pytest.raises(Exception):
        get_mask_account(1111222233334444555)


def test_get_mask_account_21_symbols():
    with pytest.raises(Exception):
        get_mask_account(111122223333444455556)


def test_get_mask_card_number_float():
    with pytest.raises(Exception):
        get_mask_account(111122223333444455.0)


def test_get_mask_card_number_negative_19_symbols():
    with pytest.raises(Exception):
        get_mask_card_number(-1111222233334444555)


@pytest.mark.parametrize("account_number, expected", [(11112222333344445555, "**5555"),
                                                   (44445555666677778888, "**8888"),
                                                   (11112222333344440000, "**0000")])
def test_get_mask_account_with_parametrize(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_fixture(get_mask_of_account):
    assert get_mask_account(11112222333344441234) == get_mask_of_account