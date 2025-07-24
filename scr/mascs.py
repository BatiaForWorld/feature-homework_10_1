"""Функцию маскировки номера банковской карты """


def get_masc_card_number(card_number: str) -> str:
    """Функция принимает на вход
    номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if len(card_number) == 16 and card_number.isdigit():
        card = str(card_number)
        card_number = card[0:4] + " " + card[4:6] + "**" + " " + "****" + " " + card[12:16]
        return card_number
    else:
        return "Введите 16 значный номер вашей карты"


"""Функцию маскировки номера банковского счета"""


def get_masc_account(account_number: str) -> str:
    """Функция принимает на вход
    номер счета  в виде числа и
    возвращает маску номера по правилу  ** XXXX"""
    if len(account_number) == 20 and account_number.isdigit():
        number = str(account_number)
        account_number = "**" + number[16:20]
        return account_number
    else:
        return "Введите 20 значный номер вашего счёта"
