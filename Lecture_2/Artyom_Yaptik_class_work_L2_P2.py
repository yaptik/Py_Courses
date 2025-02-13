# Классная работа Лекция-1 Часть-2.

# boolean (bool) logic - логические выражения.
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> a == b
False
>>> a != b
True
>>> a < b
True
>>> a <= b
True

>>> a, b = 9, 9
>>> a == b
True 
>>> a <= b  # Одно из условий верно (тут - равно), значит результат Правда.
True
>>> res = a != b
>>> res
False
>>> type(res)
<class 'bool'>

# Conditions and conditional execution.
>>> password = input("/login:")
/login:12345
>>> if password == "12345":  # Видим, что введённый и предустановленный пароли совпали.
	print("ok")

	
ok

>>> password = input("/login:")
/login:123
>>> secret = "123"  # Как бы безопасно скрытое кодовое слово.
>>> if password == secret:
	print("ok")

	
ok

# Вариант с несовпадением пароля и альтернативным действием.
password = input("/login:")
secret = "123"
if password == secret:
	print("ok")
else:
	print("not match")

# if-elif-else
amount = int(input("amount? "))
if amount < 1000:
    discount = amount * .05  # Скидка 5%.
elif amount < 5000:
    discount = amount * .1  # Скидка 10%.
else:
    discount = amount * .15  # Скидка 15%.

print("discount is: ", discount)
print("net payable: ", amount-discount)

amount? 900
discount is:  45.0
net payable:  855.0
>>> 
amount? 1001
discount is:  100.10000000000001
net payable:  900.9
>>> 
amount? 5500
discount is:  825.0
net payable:  4675.0

# Меньше строк кода.
res = True if a == 123 else False  # В одну строку вместо четерех.

# match n case.
>>> password = 'bond*'
>>> match password:
...     case "123":
...         print("ok")
...     case "bond*":
...         print("spy ok")
...     case _:
...         print (-1)
... 
spy ok

# while.
counter = 1
while counter < 10:
    print(counter)
    counter += 2  # Увеличим счетчик на 2 за проход цикла.

1
3
5
7
9

# Stop endless circle <Ctrl-Z>, <Ctrl-C>.

# Печатать всё из диапазона 5, ДО указанного числа (исключ). Шаг 1.
for i in range(5):
     print(i)
0
1
2
3
4
>>> 
for i in range(1, 6, 2):  # Начало, конец (не включается), шаг.
     print(i)
1
3
5

# Вывод с тайм-лагом 1 сек.
>>> import time
>>> time.sleep(3)
>>> for i in range(6):
     print("sleep ", i)
     time.sleep(1)

     
sleep  0
sleep  1
sleep  2
sleep  3
sleep  4
sleep  5
>>> 

# break n continue используются только внутри циклов for или while.

# in, not in.
>>> st = "hello 1234"
>>> to_find = "2"
>>> to_find in st  # in - содержится.
True
>>> to_find = "0"
>>> to_find in st
False

>>> if to_find in st:
	print("0 in st")
else:
	print("nope")

	
nope

# Lab 2.5.
# Достать из строки по одному символу и распечатать по одному символу.
>>> word = "kvpo872udla"
>>> for char in word:
	print(char)

	
k
v
p
o
8
7
2
u
d
l
a
>>> 
>>> noPrint = "asdfgh"  # Это не печатать.
>>> for char in word:
	if char in noPrint:
		continue
	print(char)

	
k
v
p
o
8
7
2
u
l  # Не напечатало из kvpo872udla символы d и a.
>>> word
'kvpo872udla'

# and - каждое условие соблюдено.
>>> >>> age = 21
>>> money = 1000
>>> if age > 18 and money > 900:
	print("GRIND")

	
GRIND

age = 16  # Мелкий возраст.
money = 1000
if age > 18 and money > 900:  # Одно из условий не соблюдено.
    print("GRIND")
else:  # Сработает else.
    print("You are so young!")
You are so young!
>>>

# or
GRIND

# True False.
>>> False or False or True
True
>>> True and True and True and False
False
>>> not True
False
>>> not not True
True
