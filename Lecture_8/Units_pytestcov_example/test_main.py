# import main
#
#
# def test_no_letters():
#     assert main.howmanyletters("") == "no data"
#
import main


def test_no_letters():
    assert main.howmanyletters("") == "no data"


def test_less_than_3_letters():
    assert main.howmanyletters("NO") == "less that three letters!?"


def test_more_that_or_3_letters():
    assert main.howmanyletters("lol :)") == ["lol", ":)"]
