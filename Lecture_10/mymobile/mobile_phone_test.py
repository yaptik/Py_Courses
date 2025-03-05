from mobile_phone import MyMobile


def test_turn_on():
    my_phone = MyMobile("8-800-555-35-35")
    assert my_phone.turn_on() == "\nMobile is on"

def test_turn_off():
    my_phone = MyMobile("8-800-555-35-35")
    my_phone.turn_on()
    assert my_phone.turn_off() == "\nMobile is off"

def test_call_when_on():
    my_phone = MyMobile("8-800-555-35-35")
    my_phone.turn_on()
    assert my_phone.call("8-800-555-35-35") == "\nCalling 8-800-555-35-35"

def test_call_when_off():
    my_phone = MyMobile("8-800-555-35-35")
    assert my_phone.call("8-800-555-35-35") == "\nMobile 8-800-555-35-35 is turned off - it's unavailable!"
