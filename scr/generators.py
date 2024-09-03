from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    """Функция принимает на вход список словарей,
    представляющих транзакции.Функция должна возвращать итератор,
    который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX , где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от
    0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и
    конечное значения для генерации диапазона номеров."""
    for num in range(start, stop + 1):
        card_number = f"{num:016d}"
        card_number = " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
        yield card_number
