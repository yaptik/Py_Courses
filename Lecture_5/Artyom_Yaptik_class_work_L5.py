# Artyom_Yaptik_class_work_L5

# import this.




>>> def hello():
	print("Hello!")

	
>>> hello
<function hello at 0x000002887785D620>
>>> hello()
Hello!
>>>  # Created func.
>>> 
>>> 
>>> def hello():
	user = input("your name:")
	print(f""Hello, {user}!")
	      
SyntaxError: invalid syntax
>>> print(f"Hello, {user}!")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(f"Hello, {user}!")
NameError: name 'user' is not defined
>>> def hello():
	user = input("your name:")
	print(f"Hello, {user}!")

	
>>> hello()
your name:anya
Hello, anya!
>>> hello()
your name: Greg
Hello, Greg!



>>> 
>>> 
>>> 
>>> def hello():
	user = input("your name:")
	print(f"Hello, {user}!")
	for i in range(3):
		print(i, end=" ")
	d = 88
	if d == 88:
		print("XXX")
	print(42346234)

	
>>> hello()
your name:sdfsd
Hello, sdfsd!
0 1 2 XXX
42346234
>>> 
>>> 


>>> 
>>> 
>>> 
>>> def hello():
	user = input("your name:")
	print(f"Hello, {user}!")
	for i in range(3):
		print(i, end=" ")
	d = 88
	if d == 88:
		print("XXX")
	print(42346234)

	
>>> hello()
your name:sdfsd
Hello, sdfsd!
0 1 2 XXX
42346234
>>> 

>>> 
>>> hello = 55
>>> hello()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable
>>> # Переназначили переменную с функции на int - вызвать нельзя.


>>> # Создать функцию.
>>> change_password()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    change_password()
NameError: name 'change_password' is not defined

# Функция без параметров.
>>> h()
>>> h(1,2,3)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    h(1,2,3)
TypeError: h() takes 0 positional arguments but 3 were given

>>> # Создали фунцкию.
>>> 
>>> 
>>> def hello():
	user = input("your name:")
	print(f""Hello, {user}!")
	      
SyntaxError: invalid syntax
>>> print(f"Hello, {user}!")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(f"Hello, {user}!")
NameError: name 'user' is not defined
>>> def hello():
	user = input("your name:")
	print(f"Hello, {user}!")

	
>>> hello()
your name:anya
Hello, anya!
>>> hello()
your name:tim
Hello, tim!
>>> 
>>> 
>>> 
>>> def hello():
	user = input("your name:")
	print(f"Hello, {user}!")
	for i in range(3):
		print(i, end=" ")
	d = 88
	if d == 88:
		print("XXX")
	print(42346234)

	
>>> hello()
your name:sdfsd
Hello, sdfsd!
0 1 2 XXX
42346234
>>> 
>>> hello = 55
>>> hello()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable
>>> # Переназначили переменную с функции на int - вызвать нельзя.
>>>
>>> 
>>> # Создать функцию.
>>> change_password()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    change_password()
NameError: name 'change_password' is not defined
>>> 
>>> def h()
SyntaxError: invalid syntax
>>> def h():
	pass

>>> h()
>>> h(1,2,3)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    h(1,2,3)
TypeError: h() takes 0 positional arguments but 3 were given
>>> 
>>> 
>>> def hello(user):
	print("Hello", user)

	
>>> hello()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'user'
>>> hello(1234)
Hello 1234
>>> hello("sdfsd")
Hello sdfsd
>>> hello(1,2,3)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    hello(1,2,3)
TypeError: hello() takes 1 positional argument but 3 were given
>>> 
.
>>> # Функция ждала один параметр.
>>> 
>>> def hello(a,b,c):
	print("Hello", a, b,c)

	
>>> hello()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    hello()
TypeError: hello() missing 3 required positional arguments: 'a', 'b', and 'c'
>>> 
>>> 
>>> hello(b=44, c=88, a=99)
Hello 99 44 88
>>> hello(33, c=88, b=44)
Hello 33 44 88
>>> b = 44
>>> hello(33, c=88, 66)
SyntaxError: positional argument follows keyword argument
>>> # Нарушен порядок передачи аргументов.
>>> 
>>> 
>>> def hello(name, age):
	print("Hello", name, age)

	
>>> hello("jojo", 28)
Hello jojo 28
>>> hello(28, "jojo")
Hello 28 jojo
>>> 
>>> # Передача аргументов по позиции.

>>> def create_order(name, ph, age=' ', msg=' '):
	print("Order 34534: created.")
	print("order details:")
	print(f"    Name:{name}")
	print(f"    Your ph:{ph}")
	print(f"    Your age:{age}")
	print(f"    Your message:{msg}")
	print()

	
>>> create_order("Goose", 123, 18, "call me!")
Order 34534: created.
order details:
    Name:Goose
    Your ph:123
    Your age:18
    Your message:call me!

>>> def a(name="Jojo", age=123):
	print(name, age)

	
>>> a()
Jojo 123
>>> a("Nata")
Nata 123
>>> 


# return.
>>> name = input("-->")
-->123124124
>>> name
'123124124'
>>> 
>>> def hello():
	pass

>>> res = hello()
>>> res
>>> print(res)
None
>>> def hello():
	print(1*44)

	
>>> res = hello()
44
>>> def create_order(name, ph, age=' ', msg=' '):
	if len(name) < 2:
		return False
	if str(ph).isallnum() != True:
		return False
	print("Order 34534: created.")
	print("order details:")
	print(f"    Name:{name}")
	print(f"    Your ph:{ph}")
	print(f"    Your age:{age}")
	print(f"    Your message:{msg}")
	print()
	return True

>>> res = create_order("", 123124)
>>> res
False
>>> res = create_order("", 123124)
>>> def create_order(name, ph, age=' ', msg=' '):
	if len(name) < 2:
		return False
	if str(ph).isalnum() != True:
		return False
	print("Order 34534: created.")
	print("order details:")
	print(f"    Name:{name}")
	print(f"    Your ph:{ph}")
	print(f"    Your age:{age}")
	print(f"    Your message:{msg}")
	print()
	return True

>>> res = create_order("UAN", 123124)
Order 34534: created.
order details:
    Name:UAN
    Your ph:123124
    Your age: 
    Your message: 

>>> def create_order(name, ph, age=' ', msg=' '):
	if len(name) < 2 or ph.isalnum() != True:
		return False
		print("Order 34534: created.")
	print("order details:")
	print(f"    Name:{name}")
	print(f"    Your ph:{ph}")
	print(f"    Your age:{age}")
	print(f"    Your message:{msg}")
	print()
	return True

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
>>> # Документация - тройные кавычки.
>>> 
>>> def a():
	print(1)

	
>>> def b():
	print(2)

	
>>> def c():
	print(3)

	
>>> c
<function c at 0x000002887785DD08>
>>> id(a)
2785144069112
>>> sss = a
>>> sss()
1
>>> id(sss)
2785144069112
>>> # Копируются функции по ссылке.
>>> 
>>> 
>>> def numbers(num):
	if num % 2 == 0:
		return True
	return None

>>> numbers
<function numbers at 0x000002887785DD90>
>>> numbers(2)
True
>>> 


>>> def numbers(num):
	if num % 2 == 0:
		return True
	return None

>>> numbers
<function numbers at 0x000002887785DD90>
>>> numbers(2)
True
>>> 

>>> 
>>> # Високосный год.
>>> # A leap year.
>>> a = 10
>>> s = "dsfsd"
>>> a
10
>>> s
'dsfsd'
>>> isinstance(a, int)
True
>>> isinstance(a, str)
False
>>> isinstance(s, int)
False
>>> isinstance(s, str)
True
>>> if isinstance(a, int):
	print("INT")
elif isinstance(a, str):
	print("STRRR")

	
INT
>>> total = 0
>>> def add_to_total(n):
	total = total + n

	
>>> add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#203>", line 2, in add_to_total
    total = total + n
UnboundLocalError: local variable 'total' referenced before assignment
>>> # Конфликт имен Global и Local
>>> 
>>> # Или в Функции. Или расписывать, чтобы не было накладок.
>>> 
>>> 
>>> 
>>> check(1.5)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    check(1.5)
NameError: name 'check' is not defined
>>> 
>>> 
>>> x = 2183
>>> def add(x):
	print("inside:", x, id(x))
	x += 8888
	print("inside:", x, id(x))

	
>>> x
2183
>>> # Плохая практика имен переменных.
>>> 
>>> x = 2183
>>> def add(number):
	print("inside:", number, id(number))
	x += 8888
	print("inside:", number, id(number))
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> def a():
	print(1)

	
>>> def b():
	print(2)

	
>>> def (c):
	
SyntaxError: invalid syntax
>>> def c():

	print(3)

	
>>> li = [a,b,c]
>>> li
[<function a at 0x000002887786F0D0>, <function b at 0x000002887786F158>, <function c at 0x000002887785DA60>]
>>> for i in li:
	i()

	
1
2
3
>>> # Засунуть функцию в список.


>>> def numbers(num):
	if num % 2 == 0:
		return True
	return None

>>> numbers
<function numbers at 0x000002887785DD90>
>>> numbers(2)
True
>>> 

>>> 
>>> # Високосный год.
>>> # A leap year.
>>> a = 10
>>> s = "dsfsd"
>>> a
10
>>> s
'dsfsd'
>>> isinstance(a, int)
True
>>> isinstance(a, str)
False
>>> isinstance(s, int)
False
>>> isinstance(s, str)
True
>>> if isinstance(a, int):
	print("INT")
elif isinstance(a, str):
	print("STRRR")

	
INT
>>> total = 0
>>> def add_to_total(n):
	total = total + n

	
>>> add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#203>", line 2, in add_to_total
    total = total + n
UnboundLocalError: local variable 'total' referenced before assignment
>>> # Конфликт имен Global и Local
>>> 
>>> # Или в Функции. Или расписывать, чтобы не было накладок.
>>> 
>>> 
>>> 
>>> check(1.5)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    check(1.5)
NameError: name 'check' is not defined
>>> 
>>> 
>>> x = 2183
>>> def add(x):
	print("inside:", x, id(x))
	x += 8888
	print("inside:", x, id(x))

	
>>> x
2183
>>> # Плохая практика имен переменных.
>>> 
>>> x = 2183
>>> def add(number):
	print("inside:", number, id(number))
	x += 8888
	print("inside:", number, id(number))
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> def a():
	print(1)

	
>>> def b():
	print(2)

	
>>> def (c):
	
SyntaxError: invalid syntax
>>> def c():

	print(3)

	
>>> li = [a,b,c]
>>> li
[<function a at 0x000002887786F0D0>, <function b at 0x000002887786F158>, <function c at 0x000002887785DA60>]
>>> for i in li:
	i()

	
1
2
3
>>> # Засунуть функцию в список.

>>> def noname(number):
	if number > 20:
		return True
	return number + noname(number+4)

>>> # Рекурсивная функция.

>>> # Фибоначчи.
>>> f1 = f2 = 1
>>> f1
1
>>> f2
1
>>> f1, f2 = f2, f1+f2
>>> f1
1
>>> f2
2
>>> f1, f2 = f2, f1+f2
>>> f1
2
>>> f2
3
>>> f1, f2 = f2, f1+f2
>>> f1
3
>>> f2
5
>>> f1 = f2 =1
>>> for i in range(10):
	f1, f2 = f2, f1+f2

	
>>> f2
144
>>> # Сумма двух предыдущих чисел.





