import main


def test_no_letters():
    assert main.howmanyletters("") == "no data"


def test_less_than_3_letters():
    assert main.howmanyletters("NO") == "less that three letters!?"