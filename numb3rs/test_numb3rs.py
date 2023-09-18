from numb3rs import validate
import pytest

def main():
    test_true()
    test_false()
def test_true():
    assert validate("1.2.3.4") ==  True
def test_false():
    assert validate("257.257.257") == False
    assert validate("255.666.666.666") == False