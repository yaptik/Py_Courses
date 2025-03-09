class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f"user name: {self.name}."

    
User.get_counter()
0
k = User("Kate")
print(k)
user name: Kate.
k.get_counter()
1
User.get_counter()
1
User.__counter
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    User.__counter
AttributeError: type object 'User' has no attribute '__counter'. Did you mean: 'get_counter'?


class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter

    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
    
    def __str__(self):
        return f"user name: {self.name}."

    
k = User("Kate")
print(k)
user name: Kate.
User.get_counter()
1
User.get_counter
<bound method User.get_counter of <class '__main__.User'>>
User.get_counter()
1
User.set_counter(55)
User.get_counter()
55
User.counter = 888
k.set_counter(66666)
User.get_counter()
66666


class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
         return f"user name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    @staticmethod
    def check_name(name):
        return False if len(name) < 2 else True

    
user1 = "Kate"
if User.check_name(user1):
    inst1 = User(user1)
else:
    print("Имя слишком короткое.")

    
print(inst1)
user name: Kate.
user2 = "J"
if User.check_name(user2):
    inst2 = User(user2)
else:
    print("Имя слишком короткое.")

    
Имя слишком короткое.

# Интересный Классовый метод.
class User:
    __counter = 0
    
    def __init__(self, name):
        print("__init__")
        self.name = name
        User.__counter += 1

    @classmethod  # Альтернативный Конструктор.
    def init_age_including(cls, name, age):  # Дадим доп параметр age.
        print("alt __init__")
        user = cls(name)
        user.age = age
        return user
    
    def __str__(self):
         return f"user name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value

        
u1 = User("Vova")
__init__
u2 = User.init_age_including("Vova", 19)  # Вызвали из Класса User доп КлассМетод.
alt __init__
__init__
User.get_counter()
2
u1.name
'Vova'
u1.age
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    u1.age
AttributeError: 'User' object has no attribute 'age'
u2.name
'Vova'
u2.age
19


# Abstract class.

# txt csv json xml
# prep export status
class ExportToTXT:
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
class ExportToCSV:
    # Вася делает свою часть кода.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")


class ExportToJson:
    # Коля делает свою часть кода.
    def __init__(self, file_name):
        self.f_n = file_name
    def export333(self):
        print("export to json", self.f_n)
    def gotovka(self):
        print("preparation")
    def check_stts(self):
        print("status")

li = [ExportToTXT("1.txt"),ExportToCSV("1.csv")]
for inst in li:
    inst.export()  # Метод export есть не везде.

Traceback (most recent call last):
  File "<pyshell#81>", line 2, in <module>
    inst.export()
AttributeError: 'ExportToTXT' object has no attribute 'export'

from abc import ABC, abstractmethod  
class Export(ABC):  # Создаём абстрактный Класс Export.
    @abstractmethod
    def export(self):
        pass
    @abstractmethod
    def prep(self):
        pass
    @abstractmethod
    def status(self):
        pass


class ExportToTXT(Export):
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
inst = ExportToTXT("asd")
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    inst = ExportToTXT("asd")
TypeError: Can't instantiate abstract class ExportToTXT with abstract methods export, prep, status


class ExportToTXT(Export):
    # Петя делает свою таску.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
inst = ExportToTXT("1.txt")
inst.status()
status
inst.prep()
prep
inst.export()
export to txt 1.txt

class ExportToJSON(Export):
    # Вася делает свою часть кода.
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to json", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
inst2 = ExportToJSON("fsd.json")
inst2.__dict__
{'file_name': 'fsd.json'}
inst2.status()
status
inst2.prep()
prep
inst2.export()
export to json fsd.json

li =[ExportToTXT("1.txt"), ExportToJSON("n1.json")]
for inst in li:
    inst.export()

    
export to txt 1.txt
export to json n1.json


# После первого перерыва.
class A:
    pass

class B(A):
    pass

class C(B):
    pass

C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

super().__init__()  # Вызов Конструктора Родительского Класса.

class A:
    a = 10

    
class B(A):
    b = 100

    
class C(B):
	c = 1000

	
c1 = C()
c1.c
1000
c1.b
100
c1.a
10
c1.d
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    c1.d
AttributeError: 'C' object has no attribute 'd'


class A:
    a = 10
    def __init__(self):
        self.aaa = 11

        
class B(A):
    b = 100
    def __init__(self):
        self.bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
c1 = C()
c1.c
1000
c1.ccc
1111
c1.b
100
c1.bbb
111
c1.a
10
c1.aaa
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    c1.aaa
AttributeError: 'C' object has no attribute 'aaa'

# Custom exceptions.
try:
    raise AttributeError
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
err
fin


try:
    1+1
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
2
ok
fin

# Работа finally.
def a(number):
    try:
        return number
    except:
        return number + 1
    else:
        return number +2
    finally:
        return number ** 10

    
a(10)
10000000000  # Отработал finally.

# Собственные Исключения + phonebook.py.
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
