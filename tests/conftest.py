import pytest

@pytest.fixture
def card_of_number():
    return "9999 88** **** 6666"


@pytest.fixture
def get_mask_of_account():
    return f"**1234"
