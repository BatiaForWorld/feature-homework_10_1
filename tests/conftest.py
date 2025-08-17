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
def transaction_description_correct() -> list[dict[str, str] | dict[str, str] | dict[str, str]]:
    return [
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def transaction_descriptions_empty_list() -> list:
    return []


@pytest.fixture
def card_number_generator_correct() -> list[str]:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


@pytest.fixture
def card_number_generator_correct_d_digit() -> list[str]:
    return [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015",
    ]


@pytest.fixture
def card_number_generator_full() -> list[str]:
    return ["9999 9999 9999 9999"]


@pytest.fixture
def card_number_generator_invalid() -> list:
    return []


@pytest.fixture(autouse=True)
def clean_log_file():
    filename = "test_log.txt"

    with open(filename, "w"):
        pass
    yield

    with open(filename, "w"):
        pass


@pytest.fixture
def tmp_json_file(tmp_path):
    def create(content):
        file_path = tmp_path / "test.json"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return str(file_path)

    return create


@pytest.fixture
def transaction_usd():
    return {"amount": "100", "currency": "USD"}


@pytest.fixture
def sample_csv_data():
    return {
        'content': "id,amount,currency,description\n1,1000.50,RUB,Покупка\n2,2500.00,USD,Перевод",
        'expected': [
            {'id': '1', 'amount': '1000.50', 'currency': 'RUB', 'description': 'Покупка'},
            {'id': '2', 'amount': '2500.00', 'currency': 'USD', 'description': 'Перевод'}
        ]
    }


@pytest.fixture
def sample_excel_transactions():
    return [
        {'id': 1, 'amount': 1000.50, 'currency': 'RUB', 'description': 'Покупка'},
        {'id': 2, 'amount': 2500.00, 'currency': 'USD', 'description': 'Перевод'}
    ]


@pytest.fixture
def file_paths_for_testing():
    return [
        'test_file.csv',
        '/absolute/path/file.csv',
        '../relative/file.csv',
        'file with spaces.csv',
        'файл_на_русском.csv'
    ]


@pytest.fixture(autouse=True)
def clean_log_file():
    filename = "test_log.txt"

    with open(filename, "w"):
        pass
    yield

    with open(filename, "w"):
        pass


@pytest.fixture
def sample_json():
    return [
        {"state": "EXECUTED", "date": "2023-01-01", "amount": "1000", "currency_name": "руб", "description": "Открытие вклада", "from": "Счет 123", "to": "Счет 456"},
        {"state": "CANCELED", "date": "2023-01-02", "amount": "2000", "currency_name": "USD", "description": "Перевод с карты на карту", "from": "Visa 1111", "to": "Mastercard 2222"},
        {"state": "EXECUTED", "date": "2023-01-03", "amount": "3000", "currency_name": "руб", "description": "Перевод организации", "from": "Счет 789", "to": "Счет 012"},
    ]
