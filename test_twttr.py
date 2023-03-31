import twttr

def main():
    test_twttr()

def test_twttr():
    assert twttr.shorten('twitter') == 'twttr'
    assert twttr.shorten('Bitcamp') == 'btcmp'
    assert twttr.shorten('tsitsagi') == 'tstsg'


if __name__ == "__main__":
    main()