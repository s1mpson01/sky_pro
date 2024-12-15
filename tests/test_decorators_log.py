from src.decorators import log


@log()
def add(x, y):
    return x + y


@log("logfile")
def adds(x, y):
    return x + y


def test_log_error(capsys):
    add("4", 5)
    captured = capsys.readouterr()
    assert "add error: can only concatenate str (not \"int\") to str. Inputs: ('4', 5), {}" in captured.out


def test_log_ok(capsys):
    add(4, 5)
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_write_file_with_ok():
    adds(4, 5)
    with open("logfile.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert content == "adds ok\n"


def test_log_write_file_with_error():
    adds("4", 5)
    with open("logfile.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert content == "adds error: can only concatenate str (not \"int\") to str. Inputs: ('4', 5), {}\n"
