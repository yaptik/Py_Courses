# Классная работа Лекция-2 Часть-1.

# Functions.
>>> input("Дай мне пароль:")  # Принять данные.
Дай мне пароль:q123
'q123'
>>> parol = input("Дай мне пароль: ")  # Сразу сохранить в переменную принятые данные.
Дай мне пароль: q123
>>> print(parol)
q123

# Сообщить инфо.
>>> msg = """qqq  
... www
... eee
...
... -->"""
>>> a = input(msg)  # Загнать ответ в переменку. 
qqq
www
eee

-->morning!
>>> print(a)  # Печать ответа.
morning!
>>> type(a)  # Узнать тип переменки.
<class 'str'>  

# types/class.
>>> a = "123"
>>> b = "3.5"
>>> c = 123
>>> d = 5.5
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> type(c)
<class 'int'>
>>> type(d)
<class 'float'>

>>> int()  # Дефолт для числа.
0
>>> str()  # Дефолт для стринг.
''
>>> float()  # Дефолт для флоат.
0.0
>>> int(d)  # Вывести д как инт, хотя он флоат.
5
>>> str(d)  # Вывести д как стринг, хотя он флоат.
'5.5'
>>> d = str(d)  # Преобразовать д в стринг вместо флоат.
>>> type(d)
<class 'str'>

>>> A = .777  # Можно не печатать 0.
>>> B = 555.  # Можно не печатать 0.
>>> print(A, B)
0.777 555.0
>>> 12 / 0  # Деление на 0.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> print(2 ** 3)  # Возвести в степень.
8
>>> print(2 ** 3.0)
8.0

# String operations.
>>> s, ss = "hello", "lol"
>>> print(s, ss)
hello lol
>>> s
'hello'
>>> ss
'lol'
>>> s + ss  
'hellolol'

>>> a = "*" * 50  # Умножить стринги - репликация, повтор.
>>> a
'**************************************************'
>>> len(a)

>>> "Garry" * 3
'GarryGarryGarry'
>>> 5 * "2"
'22222'
>>> a = "qwe" "asd" "zxc"  # Без запятых.
>>> a
'qweasdzxc'
>>> len(a)  # Длина выражения.
9
>>> b = "qwe", "asd", "zxc"  # С запятыми.
>>> b
('qwe', 'asd', 'zxc')
>>> len(b)
3

>>> a = int(input("-->"))  # Принять данные, как integer.
-->123
>>> type(a)
<class 'int'>
>>> a
123
>>> a**2  # Возвести данные в степень.
15129

# Нельзя присваивать функции int какое-то значение, как переменной.
# int = 777 - это плохо и позже наверняка вызовет TypeError: 'int' object is not callable.
# Придётся делать рестарт оболочки SHELL.

>>> print = "gggg"
>>> print(print)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable

# Python keywords.
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

pass  # Ничего не делать - обозначить, занять место для будущего блока.

# The simple calculator. In file Kuzmichev_Igor_L2-calculator.py.
# В строке максимум 79 символов!. https://peps.python.org/pep-0008/#maximum-line-length.

# PEP 20 - The Zen of Python.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
