from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_zero_division()
    test_value_error()

def test_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert gauge(1) == "E" and gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("pls/work")

