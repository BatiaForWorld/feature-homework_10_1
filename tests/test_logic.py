import pytest
from scr.logic import (
    process_bank_search,
    filter_by_status,
    filter_rub_transactions,
    sort_transactions_by_date,
    format_transaction,
)


@pytest.mark.parametrize("status,expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 0),
])
def test_filter_by_status(sample_json, status, expected_count):
    """
    Проверяет фильтрацию транзакций по статусу (EXECUTED, CANCELED, PENDING).
    Ожидает количество результатов согласно статусу.
    """
    result = filter_by_status(sample_json, status)
    assert len(result) == expected_count

@pytest.mark.parametrize("search,expected", [
    ("вклад", 1),
    ("перевод", 2),
    ("нет", 0),
])
def test_process_bank_search(sample_json, search, expected):
    """
    Проверяет поиск транзакций по ключевому слову в описании.
    Ожидает количество найденных результатов.
    """
    result = process_bank_search(sample_json, search)
    assert len(result) == expected

def test_filter_rub_transactions(sample_json):
    """
    Проверяет фильтрацию рублевых транзакций на исходных данных.
    Ожидает 2 результата (только рублевые).
    """
    result = filter_rub_transactions(sample_json)
    assert len(result) == 2

@pytest.mark.parametrize("reverse,first_date", [
    (False, "2023-01-01"),
    (True, "2023-01-03"),
])
def test_sort_transactions_by_date(sample_json, reverse, first_date):
    """
    Проверяет сортировку транзакций по дате.
    Ожидает, что первая транзакция соответствует ожидаемой дате.
    """
    result = sort_transactions_by_date(sample_json, reverse=reverse)
    assert result[0]["date"] == first_date

@pytest.mark.parametrize("transaction,expected_str", [
    ({"date": "08.12.2019", "description": "Открытие вклада", "to": "Счет **4321", "operationAmount": {"amount": "40542", "currency": {"name": "руб"}}}, "08.12.2019 Открытие вклада"),
    ({"date": "01.01.2020", "description": "Тестовая операция", "from": "Счет 12345678901234567890", "to": "Visa 1234 5678 9012 3456"}, "Сумма: нет данных"),
])
def test_format_transaction(transaction, expected_str):
    """
    Проверяет форматирование строки транзакции для вывода.
    Ожидает наличие ключевых данных в результирующей строке.
    """
    result = format_transaction(transaction)
    assert expected_str in result

# Edge-case: пустой ввод
@pytest.mark.parametrize("user_input", ["", None])
def test_process_bank_search_empty(sample_json, user_input):
    """
    Проверяет обработку пустого ввода для поиска транзакций.
    Ожидает, что вернутся все элементы.
    """
    result = process_bank_search(sample_json, user_input or "")
    assert result == sample_json
