from scr.external_api import get_transaction_amount_in_rub

import pytest
from unittest.mock import patch
import requests


@patch("requests.get")
def test_successful_conversion(mock_get, transaction_usd):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 9800.5}
    result = get_transaction_amount_in_rub(transaction_usd)
    assert result == 9800.5


@patch("requests.get")
def test_empty_result_error(mock_get, transaction_usd):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}
    with pytest.raises(ValueError, match="Empty or invalid result"):
        get_transaction_amount_in_rub(transaction_usd)


@patch("requests.get", side_effect=requests.exceptions.Timeout)
def test_api_timeout(mock_get, transaction_usd):
    with pytest.raises(TimeoutError, match="API request timed out"):
        get_transaction_amount_in_rub(transaction_usd)


@patch("requests.get")
def test_server_unavailable(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Server is unreachable")

    transaction = {"amount": "100", "currency": "USD"}

    with pytest.raises(ConnectionError) as exc_info:
        get_transaction_amount_in_rub(transaction)

    assert "API request failed" in str(exc_info.value)


@patch("requests.get")
def test_api_response_missing_rate(mock_get):
    mock_response = mock_get.return_value
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {}

    transaction = {"amount": "100", "currency": "USD"}

    with pytest.raises(ValueError):
        get_transaction_amount_in_rub(transaction)
