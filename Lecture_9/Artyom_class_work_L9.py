class Dog:
        pass

class Lada:
        pass

class Wallet:
        pass

# Экземпляры класса int.
Result: 10
Score: 1412

# Экземпляры класса float.
Result: 10.18
pi: 3.14

>>> d = Dog()
>>> type(d)
<class '__main__.Dog'>  # Пустой экземпляр.
>>> 
>>> class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

		
>>> d = Dog()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = Dog()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
>>> d = Dog("Bobik", 34)

>>> dima = User("Dima", "dima@mail.ru")
>>> type(dima)
<class '__main__.User'>


>>> class User:
	def __init__(self, name, email):
                self.name = name
                self.email = email
	

>>> dima = User("Dima", "dima@mail.com")
>>> 
>>> type(d)
<class '__main__.Dog'>
>>> isinstance(dima, User)  # Является ли dima экземпляром класса User.
True
>>> isinstance(dima, Dog)  # Является ли dima экземпляром класса Dog.
False

>>> d.age
34
>>> d.name
'Bobik'
>>> 
>>> dima = User("Dima", "dima@mail.com")
>>> vova = User("Vova", "vova@mail.com")
>>> dima.name
'Dima'
>>> vova.email
'vova@mail.com'


>>> class User:
	users_counter = 0
	def __init__(self, name, email):
		self.name = name
		self.email = email

		
>>> User.users_counter
0
>>> User.users_counter = 555
>>> User.users_counter
555
>>> User.users_counter += 1
>>> User.users_counter
556
>>> 


>>> class User:
	users_counter = 0
	def __init__(self, name, email):
		self.name = name
		self.email = email
		User.users_counter += 1  # +1 к счетчику при добавлении нового юзера.

		
>>> User.users_counter
0
>>> dima = User("Di","@")
>>> User.users_counter
1
>>> vika = User("Vi","@")
>>> User.users_counter
2
>>> 
>>> dima.name  # Переменная из Экземпляра.
'Di'
>>> User.users_counter  # Переменная из Класса.
2
>>> 

# На лету переменные создавать нежелательно - собьётся структура Экземпляра.
>>> User.jojo = 9999
>>> User.jojo
9999
>>> dima.jojo
9999

>>> 



>>> class Wallet:
	"""Представляет структуру полей для описания кошелька."""
	counter = 0
	def __init__(self, owner, currency, amount, address="", color="silver"):
		self.owner = owner
		self.currency = currency
		self.amount = amount
		self.address = address
		self.color = color
		Wallet.counter += 1
		self.wallet_id = Wallet.counter * 10

		
>>> Wallet.counter
0
>>> fw = Wallet("S F", "BYN", 1000)
>>> Wallet.counter
1
>>> fw.owner
'S F'
>>> fw.currency
'BYN'
>>> fw.amount
1000
>>> fw.address
''
>>> fw.color
'silver'
>>> fw.wallet_id
10
>>> sw = Wallet("D F", "RUB", 2000, color="GOLD")
>>> sw.owner
'D F'
>>> sw.currency
'RUB'
>>> sw.color
'GOLD'
>>> Wallet.__doc__
'Представляет структуру полей для описания кошелька.'
>>> Wallet.__name__
'Wallet'
>>> Wallet.__module__
'__main__'
>>> Wallet.__bases__
(<class 'object'>,)
>>> fw.__dict__
{'owner': 'S F', 'currency': 'BYN', 'amount': 1000, 'address': '', 'color': 'silver', 'wallet_id': 10}
>>> sw.__dict__
{'owner': 'D F', 'currency': 'RUB', 'amount': 2000, 'address': '', 'color': 'GOLD', 'wallet_id': 20}
>>> 

>>> for k, v in fw.__dict__.items():
	print(k, ":", v)

	
owner : S F
currency : BYN
amount : 1000
address : 
color : silver
wallet_id : 10
>>> 
>>> for k, v in sw.__dict__.items():
	print(k, ":", v)

	
owner : D F
currency : RUB
amount : 2000
address : 
color : GOLD
wallet_id : 20
>>> 

# Функции и методы. Function vs Methods.
# https://docs.python.org/3/tutorial/classes.html#method-objects .

>>> class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
        def hello(self, message):  # Создать метод hello.
                print(f"{self.name} says {message}!")

	
>>> d1 = User("Dima", "@")  # Создать юзера Dima.
>>> d1.name
'Dima'
>>> d1.email
'@'
>>> d1.hello
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d1.hello
AttributeError: 'User' object has no attribute 'hello'  # Думаю, изза моей версии Python 3.6. Жду 3.10.

>>> class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
	def hello(self, message):
		print(f"{self.name} says {message}!")
	def bye(self):
		print(f"{self.name} says bye bye!")

		
>>> d1 = User("Dima", "@")
>>> d1.hello("abc")
Dima says abc!
>>> d1.bye()
Dima says bye bye!

>>> st = "hello"
>>> print(st)
hello
>>> print(d1)
<__main__.User object at 0x000001E95985DD68>  # Указан адрес объекта в памяти.


>>> class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
	def hello(self, message):
		print(f"{self.name} says {message}!")
	def bye(self):
		print(f"{self.name} says bye bye!")
	def __str__(self):
		return f"User: name-{self.name}, email-{self.email}."

	
>>> kate = User("Kate", "kate@mail.com")
>>> kate.hello("abc")
Kate says abc!
>>> print(kate)
User: name-Kate, email-kate@mail.com.


>>> dir(int)  # Вывод всех методов внутри типа int.
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 

>>> dir(User)  # Тут можно увидеть созданный нами метод __hello__.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello']
>>> 

>>> 
>>> 
>>> class Storage:
	counter_id = 0
	def __init__(self):
		self.storage = {}
	def add_user(self, user):
		Storage.counter_id += 1
		self.storage.update({Storage.counter_id:user})
	def show_all(self):
		for user_id, user in self.storage.items():
			print(f"User id:{user_id}")
			print(f"Name:{user.name}")
			print(f"Email:{user.email}")
			print("__str__")
			print(user)
			print(user.bye())

			
>>> strg = Storage()
>>> dima = User("Dima", "d@em")
>>> kate = User("Kate", "k@em")
>>> vasia = User("Vasia", "v@em")
>>> strg.add_user(dima)
>>> strg.add_user(kate)
>>> strg.add_user(vasia)
>>> strg.show_all()
User id:1
Name:Dima
Email:d@em
__str__
User: name-Dima, email-d@em.
Dima says bye bye!
None
User id:2
Name:Kate
Email:k@em
__str__
User: name-Kate, email-k@em.
Kate says bye bye!
None
User id:3
Name:Vasia
Email:v@em
__str__
User: name-Vasia, email-v@em.
Vasia says bye bye!
None


# Наследование. Inheritance.
>>> class Car:
	def __init__(self, vin, volume, model_name):
		self.vin = vin
		self.volume = volume
		self.model_name = model_name
	def __str__(self):
		return "привет из родительского класса."

	
>>> class Sedan:  # Класс без родительского класса.
	pass

>>> class Wagon:
	pass

>>> s = Sedan()
>>> Sedan.__bases__
(<class 'object'>,)
>>> s
<__main__.Sedan object at 0x000001CFAA079A58>
>>> class Sedan(Car):  # Класс с родительским классом Car.
        pass

>>> class Wagon(Car):  # Класс с родительским классом Car.
	pass

>>> s = Sedan()  # Ошибка, т.к. доч.Класс уже привязан к род.Классу.
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    s = Sedan()
TypeError: __init__() missing 3 required positional arguments: 'vin', 'volume', and 'model_name'
>>> s = Sedan("44097", 1.6, "Megane")  # Внесём данные в род.Класс.
>>> print(s)
привет из родительского класса.
>>> 
>>> isinstance(s, Sedan)
True
>>> isinstance(s, Car)
True

>>> class Car:
	def __init__(self, vin, volume, model_name):
		self.vin = vin
		self.volume = volume
		self.model_name = model_name
	def __str__(self):
		return "привет из родительского класса."
	def drive(self):
		print("ВРУМ!")

		
>>> class Sedan(Car):
	pass

>>> class Wagon(Car):
	pass

>>> w = Wagon(111, 1.9, "2104")
>>> w.__dict__
{'vin': 111, 'volume': 1.9, 'model_name': '2104'}
>>> Sedan.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})
>>> Car.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function Car.__init__ at 0x000001CFAA07A950>, '__str__': <function Car.__str__ at 0x000001CFAA07A8C8>, 'drive': <function Car.drive at 0x000001CFAA07A620>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
>>> w.drive()
ВРУМ!

>>> class Sedan(Car):
		def drive(self):
			print("Седан делает трррр!")

			
>>> s = Sedan(222, 2.0, "2101")
>>> s.drive()
Седан делает трррр!


class Wagon(Car):
	pass

class Sedan(Car):
		def drive(self):
                        super().drive()
			print("Седан делает трррр!")

>>> w = Wagon(111, 1.9, "2104")
>>> s = Sedan("44097", 1.6, "Megane")
>>> w.drive()
ВРУМ!
>>> s.drive()  # Достали печать и из Родит и из Доч.классов.
ВРУМ!
Седан делает трррр!
>>> 

class Car:
	def __init__(self, vin, volume, model_name):
		self.vin = vin
		self.volume = volume
		self.model_name = model_name
	def __str__(self):
		return "привет из родительского класса."
	def drive(self):
		print("ВРУМ!")
	def show_car(self):
                print(self.vin, self.volume, self.model_name)


class Sedan(Car):
	def __init__(self, vin, volume, model_name):
		self.body_type = "Sedan"
		super().__init__(vin, volume, model_name)
	def drive(self):
		super().drive()
		print("Седан делает трррр!")

>>> w = Wagon(111, 1.9, "2104")
>>> s = Sedan("44097", 1.6, "Megane")

>>> s.vin
'44097'
>>> s.body_type
'Sedan'
>>> s.volume
1.6
>>> s.model_name
'Megane'
>>> s.show_car()
44097 1.6 Megane

# Инкапсуляция Encapsulation.

>>> money = 1001
>>> money = -1000  # Новый взломанный баланс.
>>> money
-1000
>>> money = 1001
>>> money
1001
>>> money -= 1000  # Новый взломанный баланс.
>>> money
1
>>> class wallet:
	def __init__(self, money):
		self.__money = money  # Засекьюрили.
	def read(self, secret):
		if secret == 123:
			return self.__money
		return "unauthorised"
	def add(self, amount, secret):
		if secret != 123:
			return "unauthorised"
		if amount > 0:
			self.__money += amount
		return "unauthorised"

	
>>> my_wallet = wallet(100)  # Внесли баланс.
>>> my_wallet.money
Traceback (most recent call last):
  File "<pyshell#491>", line 1, in <module>
    my_wallet.money
AttributeError: 'wallet' object has no attribute 'money'
>>> my_wallet.__money
Traceback (most recent call last):
  File "<pyshell#492>", line 1, in <module>
    my_wallet.__money
AttributeError: 'wallet' object has no attribute '__money'
>>> my_wallet.read(111)  # Неверный пароль для чтении баланса.
'unauthorised'
>>> my_wallet.read(123)  # Верный пароль для чтения баланса.
100
>>> my_wallet.add(-111, 200)
'unauthorised'
>>> my_wallet.add(-111, 500)
'unauthorised'
>>> my_wallet.add(555, 123)  # Прибавка к сумме. Верный пароль.
'unauthorised'
>>> my_wallet.read(123)
655  # Отобразили баланс.

# Для нежелательных к использованию.
_name
# Для совсем приватных имён переменных.
__name
# Для исключения перезаписи.
name_
# Для служебных методов.
__name__
