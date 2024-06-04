def mask_card_number(card_number: int) -> str:
    """Преобразуем номер карты в строку"""
    card_number_str = str(card_number)
    """ Маскируем номер карты """
    masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[-4:]
    return masked_card


def mask_account_number(account_number: int) -> str:
    """Преобразуем номер счета в строку"""
    account_number_str = str(account_number)
    """ Маскируем номер счета """
    masked_account = "**" + account_number_str[-4:]
    return masked_account
