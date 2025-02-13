# Классная работа Лекция 1.

# my first program.
print("Hello, World!")  # вывод текста.

# сместить часть текста с новой строки.
print("Hello world\nits a day for beginning")  # делим текст на с новой строки.
print() # пустая строка.
print("down came rain\nand washed the spider out")  # делим текст на с новой строки.

# множественные аргументы.
print("the itsy bitsy spider" , "climbed up" , "the waterspout.")  # несколько аргументов.

# множ аргументы и две строки.
print("My name is" , "Python. ")
print("Monty Python. ")

# разделитель и окончание.
print("My name is" , "Python." , end=" ")
print("Monty Python. ")
print("My" , "name" , "is" , "Monty" , "Python." , sep="-")  # внести "-" между слов.
print("My" , "name" , "is" , sep="_" , end="*")
print("Monty" , "Python." , sep="*" , end="\n")

# Literals.
print(123)
print(11_111)
print(-6335)
print(0o231)  # 153 in octal.
print(0o123)  # 83 in octal.
print(0x123)  # 291 inhexadecimal.
print(2,3)
print(2.3)  # float.
print(3E8)  # 8 нулей после 3.

# Strings.
print("Привет Петька'c")
print('Привет Петька\'c')

# Boolean.
print(True > False)  # булевые операции.
print(True < False)

# Variables.
x = 5
y = "John"
print(x)  # печатаем значение х.
print(y)

x = 4  # type integer.
x = "Sally"  # type string.

y = "John"  # двойные кавычки есть как одинарные.
print(y)
y = 'John'
print(y)
print()

# Arithmetic.
a = 1
b = 5
print(a+b)  # арифметические операторы.
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
print()

a = 1
print(a)  # арифметические операторы.
a += 3
print(a)
a *= 2
print(a)
print()

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print()

a = 0.35459
print(round(a, 2))  # округление до числа после запятой.
print(round(a, 4))
print()
