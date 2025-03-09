class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
         return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            pass
        return f"звони {number}"

    
class NumberError(Exception):
    def __init_(self, number, message):
        self.number = number
        self.message = message

        
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
         return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, "Короткий номер!")
        return f"звони {number}"

    
user1 = User("Vasia")
user1.call(1223)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    user1.call(1223)
  File "<pyshell#190>", line 7, in call
    if len(number) < 8:
TypeError: object of type 'int' has no len()
user1.call("1223")  # Как строка.
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    user1.call("1223")
  File "<pyshell#190>", line 8, in call
    raise NumberError(number, "Короткий номер!")
NumberError: ('1223', 'Короткий номер!')


try:
    user1.call("1223")
except NumberError as e:
    print(e)
except:
    print("-1")

    
('1223', 'Короткий номер!')


class NumberError(Exception):
    def __init_(self, number, message):
        self.number = number
        self.message = message
    def __str__(self):
        return f"NumberError: number: {self.number}, message: {self.message}"


class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
         return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, "Короткий номер!")
        return f"звоню {number}"

    
user1 = User("Vasia")
try:
    user1.call("1223")
except NumberError as e:
    print(e)
except:
    print("-1")

NumberError: number: 1223, message: Короткий номер!
