>>> import datetime
>>> datettime.datetime.now()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    datettime.datetime.now()
NameError: name 'datettime' is not defined. Did you mean: 'datetime'?
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2025, 3, 5, 19, 46, 47, 267457)
>>> print(datetime.now())
2025-03-05 19:47:15.305547
>>> def decorator(func):
...     def inner(dname):
...         print('привет из декоратора')
...         print('время', datetime.now())
...         print('имя функции', func.__name__)
... 
...         
>>> @decorator
... def say(n):
...     print(f'{n}, привет')
... 
...     
>>> @decorator
... def bay(n):
...     print(f'{n}, пока')
... 
...     
>>> bye('Petya')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    bye('Petya')
NameError: name 'bye' is not defined
>>> say('dasas')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    say('dasas')
TypeError: 'NoneType' object is not callable
>>> def decorator(func):
...     def inner(dname):
...         print('привет из декоратора')
...         print('время', datetime.now())
...         print('имя функции', func.__name__)
...         func(dname)
...     return inner
... 
>>> @decorator
... def say(n):
...     print(f'{n}, привет')
... 
...     
>>> @decorator
... def bay(n):
...     print(f'{n}, пока')
... 
...     
>>> say('dasas')
привет из декоратора
время 2025-03-05 19:53:47.963549
имя функции say
dasas, привет
>>> bye('Petya')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    bye('Petya')
NameError: name 'bye' is not defined
>>> bay('Petia')
привет из декоратора
время 2025-03-05 19:54:19.270180
имя функции bay
Petia, пока
