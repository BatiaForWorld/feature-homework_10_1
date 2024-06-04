from scr.mascs import mask_account_number, mask_card_number


def mask_info(info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа информации"""
    if "Счет" in info:
        account_number = int(info.split()[-1])
        return "Счет " + mask_account_number(account_number)
    else:
        card_number = int("".join(info.split()[2:]).replace(" ", ""))
        return " ".join(info.split()[:2]) + " " + mask_card_number(card_number)


""" Примеры использования функции """
info1 = "Visa Platinum 7000 7922 8960 6361"
info2 = "Счет 73654108430135874305"

print(mask_info(info1))
print(mask_info(info2))

"""Функция, которая принимает на вход строку вида
 2018-07-11T02:26:18.671407
 и возвращает строку с датой в виде
11.07.2018"""


def format_date(date_str: str) -> str:
    """Разбиваем строку на части по символу 'T'"""
    date_part = date_str.split("T")[0]
    """Разбиваем дату на составные части"""
    year, month, day = map(int, date_part.split("-"))
    """Форматируем дату в нужный формат"""
    formatted_date = f"{day:02d}.{month:02d}.{year}"
    return formatted_date


"""Пример использования функции"""
date_input = "2018-07-11T02:26:18.671407"
print(format_date(date_input))
