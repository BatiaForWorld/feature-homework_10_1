import json
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(json_path: str):
    """
    Загружает список финансовых транзакций из JSON-файла.
    Возвращает список словарей. Если файл пустой, не найден или не содержит список — возвращает пустой список.
    """
    logger.info(f"Попытка загрузки транзакций из файла: {json_path}")

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                result = [item for item in data if isinstance(item, dict)]
                logger.info(f"Успешно загружено {len(result)} транзакций из файла {json_path}")
                return result
            else:
                logger.error(f"Файл {json_path} не содержит список. Тип данных: {type(data)}")
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка при загрузке файла {json_path}: {str(e)}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке файла {json_path}: {str(e)}")

    return []
