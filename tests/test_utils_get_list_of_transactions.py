import json
from unittest.mock import mock_open, patch

from src.utils import get_list_of_transactions

mock_data = [{"key": "value"}]


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_data))
def test_read_json_file(mock_file):
    result = get_list_of_transactions("12")
    assert result == mock_data


mock_data_2 = []


@patch("builtins.open", new_callable=mock_open, read_data=None)
def test_read_empty_file(mock_file):
    result = get_list_of_transactions("12")
    assert result == mock_data_2


def test_read_json_with_incorrect_path():
    result = get_list_of_transactions("no_path")
    assert result == []
