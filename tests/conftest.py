import pytest


@pytest.fixture
def card_of_number():
    return "9999 88** **** 6666"


@pytest.fixture
def get_mask_of_account():
    return f"**1234"


@pytest.fixture
def account_mask():
    return f"Счет **4305"


@pytest.fixture
def data_string_fixture():
    return f"1999-03-11T02:26:18.321407"