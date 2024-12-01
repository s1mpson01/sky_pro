import pytest

from src.processing import filter_by_state


def test_filter_by_state_with_fixture(filter_by_state_fixture):
    assert filter_by_state(filter_by_state_fixture) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "my_list, parameter, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_filter_by_state_with_parametrize(my_list, parameter, expected):
    assert filter_by_state(my_list, parameter) == expected


def test_filter_state_without_key_state():
    assert (
        filter_by_state(
            [
                {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            ],
            "EXECUTED",
        )
        == []
    )


def test_filter_state_empty():
    assert filter_by_state([], "START") == []


def test_filter_state_with_not_default_key():
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "20319-07-03T18:35:29.512364"},
            {"id": 939723570, "state": "EXECUTED", "date": "20318-06-30T0232:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "20318-09-1232T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "20318-10-1432T08:21:33.419441"},
        ],
        "CANCELED",
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "20318-09-1232T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "20318-10-1432T08:21:33.419441"},
    ]


def test_filter_state_isinstance():
    with pytest.raises(Exception):
        assert filter_by_state(
            {"id": 939723570, "state": "EXECUTED", "date": "20318-06-30T0232:08:58.425572"}, "EXECUTED"
        )
