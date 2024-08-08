import pytest

from scr.mascs import get_masc_account, get_masc_card_number


@pytest.mark.parametrize(
    "value, expected",
    [("1234567890123456", "1234 56** **** 3456"), ("1234567890", "Введите 16 значный номер вашей карты")],
)
def test_get_masc_card_number_(value: str, expected: str) -> None:
    assert get_masc_card_number(value) == expected


def test_get_masc_card_number(correct_masc_card: str) -> None:
    assert get_masc_card_number("1234567890123456") == correct_masc_card


def test_get_masc_card_number_invalid(invalid_masc_card: str) -> None:
    assert get_masc_card_number("12j3jflv") == invalid_masc_card


def test_get_masc_account(get_masc_account_correct: str) -> None:
    assert get_masc_account("12345678901234567890") == get_masc_account_correct


def test_get_masc_account_invalid(get_masc_account_wrong: str) -> None:
    assert get_masc_account("sdfgdsgeq34WFwr") == get_masc_account_wrong
