def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает на вход список словарей и значение для ключа
state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
 содержащий только те словари, у которых ключ state
 содержит переданное в функцию значение."""
    return [i for i in data if i["state"] == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
 в котором исходные словари отсортированы по убыванию даты (ключ date).
 Функция принимает два аргумента,
  второй необязательный задает порядок сортировки (убывание, возрастание)."""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
