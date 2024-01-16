from plates import is_valid

def main():
    test_singledigit()
    test_onlyalpha()
    test_puntuaction()
    test_works()
    test_0placement()
    test_numberplacement()
    test_start()

def test_singledigit():
    assert is_valid("H") == False
def test_onlyalpha():
    assert is_valid("OUTATIME") == False
def test_puntuaction():
    assert is_valid("PI3.14") == False
def test_works():
    assert is_valid("ECTO88") == True
def test_0placement():
    assert is_valid("CS05") == False
def test_numberplacement():
    assert is_valid("CS50P2") == False
def test_start():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
