import pytest


@pytest.fixture
def correct_masc_card() -> str:
    return "1234 56** **** 3456"


@pytest.fixture
def invalid_masc_card() -> str:
    return "Введите 16 значный номер вашей карты"


@pytest.fixture
def get_masc_account_correct() -> str:
    return "**7890"


@pytest.fixture
def get_masc_account_wrong() -> str:
    return "Введите 20 значный номер вашего счёта"


@pytest.fixture
def masc_card_correct() -> str:
    return "Master Card 1234 56** **** 3456"


@pytest.fixture
def masc_account_correct() -> str:
    return "Счёт **7890"


@pytest.fixture
def masc_card_wrong_format() -> str:
    return "Введите корректные данные"
