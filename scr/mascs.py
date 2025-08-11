import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""Функцию маскировки номера банковской карты """


def get_masc_card_number(card_number: str) -> str:
    """Функция принимает на вход
    номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    logger.info(f"Вызов функции маскировки номера карты. Длина входных данных: {len(card_number)}")

    if len(card_number) == 16 and card_number.isdigit():
        card = str(card_number)
        card_number = card[0:4] + " " + card[4:6] + "**" + " " + "****" + " " + card[12:16]
        logger.info(f"Успешно замаскирован номер карты")
        return card_number
    else:
        logger.error(f"Некорректный номер карты. Длина: {len(card_number)}, является числом: {card_number.isdigit()}")
        return "Введите 16 значный номер вашей карты"


"""Функцию маскировки номера банковского счета"""


def get_masc_account(account_number: str) -> str:
    """Функция принимает на вход
    номер счета  в виде числа и
    возвращает маску номера по правилу  ** XXXX"""
    logger.info(f"Вызов функции маскировки номера счета. Длина входных данных: {len(account_number)}")

    if len(account_number) == 20 and account_number.isdigit():
        number = str(account_number)
        account_number = "**" + number[16:20]
        logger.info(f"Успешно замаскирован номер счета")
        return account_number
    else:
        logger.error(
            f"Некорректный номер счета. Длина: {len(account_number)}, является числом: {account_number.isdigit()}"
        )
        return "Введите 20 значный номер вашего счёта"
