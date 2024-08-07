from scr.widget import get_date, masc_account_card


def test_masc_card(masc_card_correct: str) -> None:
    assert masc_account_card("Master Card 1234567890123456") == masc_card_correct


def test_masc_account(masc_account_correct: str) -> None:
    assert masc_account_card("Счёт 12345678901234567890") == masc_account_correct


def test_masc_account_card_invalid(masc_card_wrong_format: str) -> None:
    assert masc_account_card("314rwe3edq13") == masc_card_wrong_format


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-3-1T02:26:18.671407") == "01.03.2024"
