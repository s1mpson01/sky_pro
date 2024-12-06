import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start_number, end_number, expected",
    [(1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])],
)
def test_generators_card_number_with_parametrize(start_number, end_number, expected):
    assert list(card_number_generator(1, 4)) == expected


def test_generators_card_number_with_fixture(card_number_fixture):
    assert list(card_number_generator(9999999999999995, 10000000000000000)) == card_number_fixture


def test_generators_card_number_with_float():
    with pytest.raises(Exception):
        assert list(card_number_generator(1.0, 3.0))


def test_generators_card_number_with_1_greater_2():
    with pytest.raises(Exception):
        assert list(card_number_generator(4, 3))


def test_generators_card_number_with_negative_number():
    with pytest.raises(Exception):
        assert list(card_number_generator(-8, -5))


def test_generators_card_number_with_upper_limit():
    with pytest.raises(Exception):
        assert list(card_number_generator(100000000000000000000, 100000000000000000002))
