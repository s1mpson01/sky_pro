from unittest.mock import patch

import pandas as pd
import pytest

from src.reading import get_transactions_from_excel

mock_data = [
    {"key": "value", "key_1": "value_1", "key_3": "value_3"},
    {"key": "value_4", "key_1": "value_5", "key_3": "value_6"},
]


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame(mock_data)
    result = get_transactions_from_excel("path_to_file")
    assert result == mock_data


def test_get_get_transactions_from_incorrect_path():
    with pytest.raises(Exception):
        assert get_transactions_from_excel("12.json")
