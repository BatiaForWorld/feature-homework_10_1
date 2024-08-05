import pytest


@pytest.fixture
def test_get_masc_card_correct():
    return "1234 56** **** 3456"


@pytest.fixture
def test_get_masc_card_invalid():
    return "Введите 16 значный номер вашей карты"

@pytest.fixture
def test_get_masc_account_correct():
    return "**7890"

@pytest.fixture
def test_get_masc_account_wrong():
    return "Введите 20 значный номер вашего счёта"


@pytest.fixture
def test_masc_card_correct():
    return "Master Card 1234 56** **** 3456"


@pytest.fixture
def test_masc_account_correct():
    return "Счёт **7890"


@pytest.fixture
def test_masc_card_wrong_format():
    return "Введите корректные данные"
