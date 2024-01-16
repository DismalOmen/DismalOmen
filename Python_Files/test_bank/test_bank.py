from bank import value

def main():
    test_0()

def test_0():
    assert value("Hello") == 0
def test_20():
    assert value("How's your day going?") == 20
def test_100():
    assert value("uwu") == 100