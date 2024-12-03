import pytest

from src.masks import get_mask_account


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
        get_mask_account(-1111222233334444555)


@pytest.mark.parametrize(
    "account_number, expected",
    [(11112222333344445555, "**5555"), (44445555666677778888, "**8888"), (11112222333344440000, "**0000")],
)
def test_get_mask_account_with_parametrize(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_fixture(get_mask_of_account):
    assert get_mask_account(11112222333344441234) == get_mask_of_account
