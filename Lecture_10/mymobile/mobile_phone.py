class MyMobile:
    def __init__(self, number):
        self.number = number
        self.switch = False
    def turn_on(self):
        self.switch = True
        return f"\nMobile is on"
    def turn_off(self):
        self.switch = False
        return f"\nMobile is off"
    def call(self, calling):
        if self.switch:
            return f"\nCalling {calling}"
        else:
            return f"\nMobile {self.number} is turned off - it's unavailable!"
