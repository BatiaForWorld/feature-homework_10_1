import json
from typing import List, Dict


def load_transactions(json_path: str) -> List[Dict]:
    """
    Загружает список финансовых транзакций из JSON-файла.
    Возвращает список словарей. Если файл пустой, не найден или не содержит список — возвращает пустой список.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict)]
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        pass

    return []


"""Проверка работы функции"""
#operations = load_transactions("../data/operations.json")
#print(f"Загружено операций: {len(operations)}")
