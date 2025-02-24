from is_odd_or_even_module import is_odd_or_even


def test_is_odd_or_even_2():
    assert is_odd_or_even(2) == True, "error case: 2"


def test_is_odd_or_even_3():
    assert is_odd_or_even(3) == False, "error case: 3"


def test_is_odd_or_even_23():
    assert is_odd_or_even(23) == True, "error case: 23"


def test_is_odd_or_even_0():
    assert is_odd_or_even(0) == True, "error case: 0"


def test_is_odd_or_even_4():
    assert is_odd_or_even(-4) == True, "error case: -4"
