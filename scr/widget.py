from scr.mascs import get_masc_account, get_masc_card_number

"""функция, которая умеет обрабатывать информацию
    как о картах, так и о счетах."""


def masc_account_card(info: str) -> str:
    info_masc = info.split()
    if len(info_masc[-1]) == 20:
        return "Счёт" + " " + get_masc_account(info_masc[-1])
    elif len(info_masc[-1]) == 16:
        return " ".join(info_masc[:-1]) + " " + get_masc_card_number(info_masc[-1])
    else:
        return "Введите корректные данные"


"""Функция, которая принимает на вход строку с датой: 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """


def get_date(date: str) -> str:
    """Разбиваем строку на части по символу 'T'"""
    date_only = date.split("T")[0]
    year, month, day = map(int, date_only.split("-"))
    """Объединяем дату на: число, месяц, год."""
    formated_date = f"{day:02d}.{month:02d}.{year}"
    return formated_date
