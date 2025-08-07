import json
from unittest.mock import patch, mock_open

import pytest
from scr.utils import load_transactions



def test_valid_json_list():
    mock_data = json.dumps([{"id": 1}, {"id": 2}])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions("data/operations.json")
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(item, dict) for item in result)


def test_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        result = load_transactions("data/operations.json")
        assert result == []


def test_non_list_json_root():
    mock_data = json.dumps({"id": 1, "amount": 100})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions("data/operations.json")
        assert result == []


def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("data/operations.json")
        assert result == []


def test_invalid_json_format():
    with patch("builtins.open", mock_open(read_data="{invalid_json}")):
        result = load_transactions("data/operations.json")
        assert result == []
