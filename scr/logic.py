"""
  МОдуль выполняет логику для обработки банковских транзакций:
- поиск по описанию
- подсчет по категориям
- фильтрация по статусу и валюте
- сортировка и форматирование
"""

import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
        Функция, которая принимает список словарей с
    данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [item for item in data if pattern.search(str(item.get("description", item.get("Описание", ""))))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций по категориям (по полю description) с помощью регулярных выражений.
    """
    counter = Counter()
    for item in data:
        desc = str(item.get("description", item.get("Описание", "")))
        for cat in categories:
            if re.search(cat, desc, re.IGNORECASE):
                counter[cat] += 1
    return dict(counter)


def filter_by_status(data: list[dict], status: str) -> list[dict]:
    """
    Фильтрует операции по статусу (state) без учета регистра и лишних пробелов.
    """
    status_upper = status.strip().upper()
    result = []
    for item in data:
        item_status = str(item.get("state", "")).strip().upper()
        if item_status == status_upper:
            result.append(item)
    return result


def filter_rub_transactions(data: list[dict]) -> list[dict]:
    """
    Фильтрует только рублевые операции с помощью регулярного выражения.
    """
    pattern = re.compile(r"руб", re.IGNORECASE)
    result = []
    for item in data:
        currency = item.get("currency_name", "") or item.get("currency_code", "") or item.get("currency", "")
        if "operationAmount" in item:
            op = item["operationAmount"]
            currency_nested = op.get("currency", {}).get("name", "")
            if pattern.search(currency_nested):
                result.append(item)
                continue
        if pattern.search(currency):
            result.append(item)
            continue
        amount_str = str(item.get("amount", ""))
        if pattern.search(amount_str):
            result.append(item)
    return result


def sort_transactions_by_date(data: list[dict], reverse: bool = False) -> list[dict]:
    """
    Сортирует операции по дате.
    """
    return sorted(data, key=lambda x: x.get("date", x.get("Дата", "")), reverse=reverse)


def format_transaction(transaction: dict) -> str:
    """
    Форматирует одну транзакцию для вывода.
    """
    import re
    from datetime import datetime

    ''' Дата '''
    date_raw = transaction.get("date", transaction.get("Дата", ""))
    date = date_raw
    try:
        if "T" in date_raw:
            date = datetime.fromisoformat(date_raw.replace("Z", "")).strftime("%d.%m.%Y")
        elif re.match(r"\d{4}-\d{2}-\d{2}", date_raw):
            date = datetime.strptime(date_raw[:10], "%Y-%m-%d").strftime("%d.%m.%Y")
    except Exception:
        pass
    description = transaction.get("description", transaction.get("Описание", ""))

    def mask_account(acc: str) -> str:
        """
        Маскирует номер счета или карты для безопасного отображения.
        """
        if not acc:
            return ""
        acc = str(acc)
        card_match_pref = re.search(
            r"(Visa|MasterCard|Discover|American Express|Maestro|JCB|UnionPay)\s(\d{4})\s(\d{4})\s(\d{4})\s(\d{4})",
            acc,
        )
        if card_match_pref:
            prefix = card_match_pref.group(1)
            return (
                f"{prefix} {card_match_pref.group(2)} {card_match_pref.group(3)[:2]}** **** {card_match_pref.group(5)}"
            )
        if acc.startswith("Счет") or acc.startswith("Счёт"):
            digits = re.sub(r"\D", "", acc)
            return f"Счет **{digits[-4:]}" if digits else acc
        card_match = re.search(r"(\d{4})\s?(\d{2})\d{2}\s?\d{4}\s?(\d{4})$", acc)
        if card_match and card_match.lastindex == 4:
            return f"{card_match.group(1)} {card_match.group(2)}** **** {card_match.group(4)}"
        return acc

    from_acc = mask_account(transaction.get("from", transaction.get("Откуда", "")))
    to_acc = mask_account(transaction.get("to", transaction.get("Куда", "")))
    amount = None
    currency = None
    if "operationAmount" in transaction:
        op = transaction["operationAmount"]
        amount = op.get("amount", "")
        currency = op.get("currency", {}).get("name", "")
    if not amount:
        amount = transaction.get("amount", transaction.get("Сумма", ""))
    if not currency:
        currency = (
            transaction.get("currency_name", "")
            or transaction.get("currency_code", "")
            or transaction.get("currency", transaction.get("Валюта", ""))
        )
    try:
        if isinstance(amount, str) and re.match(r"^\d+\.\d+$", amount):
            amount = str(int(float(amount)))
    except Exception:
        pass
    lines = [f"{date} {description}".strip()]
    if from_acc and to_acc:
        lines.append(f"{from_acc} -> {to_acc}")
    elif from_acc:
        lines.append(f"{from_acc}")
    elif to_acc:
        lines.append(f"{to_acc}")
    if amount and currency:
        lines.append(f"Сумма: {amount} {currency}".strip())
    else:
        lines.append("Сумма: нет данных")
    return "\n".join(lines)
