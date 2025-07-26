import json
import pytest
from scr.utils import load_transactions


@pytest.mark.parametrize(
    "content,expected",
    [
        ('[{"amount": 100, "type": "income"}]', [{"amount": 100, "type": "income"}]),
        ('[]', []),
        ('', []),
        ('{}', []),
        ('{"amount": 100}', []),
        ('invalid json', []),
    ]
)
def test_load_transactions_various_cases(tmp_json_file, content, expected):
    path = tmp_json_file(content)
    assert load_transactions(path) == expected


def test_load_transactions_file_not_found():
    assert load_transactions("non_existent_file.json") == []


def test_load_transactions_oserror(monkeypatch, tmp_path):
    # Simulate OSError (e.g., permission denied)
    file_path = tmp_path / "test.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write('[{"amount": 100}]')

    def raise_oserror(*args, **kwargs):
        raise OSError("Permission denied")

    monkeypatch.setattr("builtins.open", raise_oserror)
    assert load_transactions(str(file_path)) == []


def test_load_transactions_multiple_items(tmp_json_file):
    data = [
        {"amount": 100, "type": "income"},
        {"amount": 50, "type": "expense"}
    ]
    path = tmp_json_file(json.dumps(data))
    assert load_transactions(path) == data
