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


@pytest.fixture
def transaction_description_correct():
    return [
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def transaction_descriptions_empty_list():
    return []


@pytest.fixture
def card_number_generator_correct():
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


@pytest.fixture
def card_number_generator_correct_d_digit():
    return [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015",
    ]


@pytest.fixture
def card_number_generator_full():
    return ["9999 9999 9999 9999"]


@pytest.fixture
def card_number_generator_invalid():
    return []
