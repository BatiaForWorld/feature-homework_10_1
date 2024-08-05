import pytest

from scr.mascs import get_masc_account, get_masc_card_number


@pytest.mark.parametrize('value, expected', [
    ('1234567890123456', '1234 56** **** 3456'),
    ('1234567890', 'Введите 16 значный номер вашей карты')
])
def test_get_masc_card_number_(value, expected):
    assert get_masc_card_number(value) == expected

def test_get_masc_card_number(test_get_masc_card_correct):
    assert get_masc_card_number("1234567890123456") == test_get_masc_card_correct


def test_get_masc_card_number_invalid(test_get_masc_card_invalid):
    assert get_masc_card_number("12j3jflv") == test_get_masc_card_invalid


def test_get_masc_account(test_get_masc_account_correct):
    assert get_masc_account("12345678901234567890") == test_get_masc_account_correct


def test_get_masc_account_invalid(test_get_masc_account_wrong):
    assert get_masc_account("sdfgdsgeq34WFwr") == test_get_masc_account_wrong
