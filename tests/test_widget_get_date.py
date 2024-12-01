import pytest

from src.widget import get_date


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