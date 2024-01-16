from twttr import shorten

def main():
    test_all()

def test_all():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("!?.,_") == "!?.,_"
    assert shorten("1234") == "1234"


if __name__ == "__main__":
    main()