from scr.decorators import log


def test_success_logging_to_file():
    @log(filename="test_log.txt")
    def add(a, b):
        return a + b

    result = add(3, 4)
    assert result == 7

    with open("test_log.txt", "r") as f:
        content = f.read().strip()
    assert content == "add ok"


def test_error_logging_to_file():
    @log(filename="test_log.txt")
    def div(a, b):
        return a / b


    result = div(10, 0)
    assert result is None

    with open("test_log.txt", "r") as f:
        content = f.read().strip()
    assert content.startswith("div error:") and "division by zero" in content


def test_success_logging_to_console(capsys):
    @log()
    def multiply(a, b):
        return a * b

    result = multiply(2, 5)
    assert result == 10

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_error_logging_to_console(capsys):
    @log()
    def faulty():
        raise ValueError("test error")

    result = faulty()
    assert result is None

    captured = capsys.readouterr()
    assert "faulty error: test error" in captured.out
