import json


def load_transactions(json_path: str) -> list[list]:
    """
    Загружает список финансовых транзакций из JSON-файла.
    Возвращает список словарей. Если файл пустой, не найден или не содержит список — возвращает пустой список.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = f.read()
            if not data.strip():
                return []
            obj = json.loads(data)
            if isinstance(obj, list):
                return obj
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []
