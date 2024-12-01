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

@pytest.fixture
def filter_by_state_fixture():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
