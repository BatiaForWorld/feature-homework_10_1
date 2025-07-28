import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CONVERT_URL = "https://api.apilayer.com/exchangerates_data/convert"

def get_transaction_amount_in_rub(transaction: dict) -> float:
    amount = float(transaction.get("amount", 0.0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    if not API_KEY:
        raise EnvironmentError("API_KEY is not set in environment")

    headers = {"apikey": API_KEY}
    params = {"from": currency, "to": "RUB", "amount": amount}

    try:
        response = requests.get(CONVERT_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data.get("result"):
            raise ValueError("Empty or invalid result in API response")

        return float(data["result"])

    except requests.exceptions.Timeout:
        raise TimeoutError("API request timed out")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"API request failed: {e}")
