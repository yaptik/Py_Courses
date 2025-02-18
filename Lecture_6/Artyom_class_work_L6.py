## L6

# li  = []
# print(type(li))
#
# tp =()
# print(type(tp))

# tp2 = tuple()  # Пустой кортеж. Функция конструктор.
# print(type(tp2))

# num = 2.  # num = (2,).
# print(type(num))
# num = 2,
# print(type(num))

# tuple(1)  # Ошибка.

# t = (1, 2)
# print(isinstance(t, tuple))

# t1 = 1.,  # Кортеж.

# n = (1, 2, 3, 5)  # Упаковка.

# n = (1, 2, 3, 4, 5)  # Конвертация для изменения.
# print(n[0])
# liN = list(n)
# liN[2] = 333
# n = tuple(liN)
# print(n)

# n = (1, 2, 3, 5, [1,2,3,4])
# n[3].append(666)
# print(n)

# t = (1, 2, 3)  # Распаковка применима ко всем послед.
# a,b,c = t
# print(b, a, c)

# t = (1, 2, 3, 4, 5, 6, 7)  # Если переменных меньше ставим "*".
# a,b,*c = t
# print(b, a, type(c))
# *a,b,c = t
# print(b, a, c)
#
# se = {1, 2, 3, 5, 6, 9, 8, 7, 8}
# a, *b, c = se
# print(b, a, c)

# def numbers():
#     return 1, 2, 3, 4
# print(numbers())
# a, *b = numbers()
# print(b, a)

# def numbers():
#     return "Err", 1, 2, 3, 4
#
#
# err, *tp_n = numbers()
# print(err, *tp_n)
# if err == "Err":
#     print("Err")

## Срезы.
# t = (1, 2, 3, 5, 6, 9, 8, 7, 8)
# print(t[:])
# aaa = t
# aaa[1] = 99   # Err.

# t = (1, 2, 3, 5, 6, 9, 8, 7, 8)
# print(t[1:])
# print(t[1:5])
# print(t[1:-1])
# print(t[::2])
# print(t[::-2])

# t = (1, 2, 3, 5, 6, 9, 8, 7, 8)
# #t += 1 # Err
# t += (1,)  # Sum.
# print(t)
# print(t*6)
# print(5 in t)

# ordersid = (1, 2, 3, 4, 5, 6)
# ordersid += (len(ordersid)+1, )
# print(ordersid)
# print(len(ordersid))

# t = (1, 2, 3, 4)  # Замена.
# print(t[1:3])
# (155, )
# (144, )
# t = (155,) + t[1:3] + (144,)
# print(t)
# print(t.count(2))
# print(t.index(144))
# # # del t
#
# t = (4, 3, 5)
# for value in t:
#     if value *2 == 4:
#         continue
#     print(value)

## fori in range(n):  # По индексу.
##     print(i, ", value:", t[i])

## Словари.
# di = {}
# type(di)
# dil1 = dict()
# type(di1)

# di = {1: "value", "sd":123}
# print(di)
# ##hash()
#
# a = 3
# b = 4.
# c = "dfdf"
# li = [1, 2, 3]
# se = {3, 2, 3, 4}
# tp = (1, 3, 2, 5)
# print(hash(a))
# print(hash(c))
# #print(hash(li))
# #print(hash(se))
# print(hash(tp))
# #print(hash(di))

# dd = {1:"a", 2.:"dfdf", "s":"dfdfdf", "fs":"froz set"}
# print(dd)
# print(dd[1])
# print(dd["s"])
# print(dd["fs"])

# dd = {1:"a", 2.:"dfdf", "s":"dfdfdf", "fs":"froz set"}  # Переборы.
# for v in dd.values():
#     print(v)
# for v in dd.keys():
#     print(v)
# for k, v in dd.items():
#     print(k, ":", v)
# print(dd.get(1))  # Достать значения.
# dd[-4] = "dfdfdfdfdf"
# for k, v in dd.items():
#     print(k, ":", v)
# dd[0] = 0
# for k, v in dd.items():
#     print(k, ":", v)
#
# dd[1] = 1323
# print(dd)
# dd.update({55:"555555"})
# print(dd)

# dd = {1:"a", 2.:"dfdf", "s":"dfdfdf", "fs":"froz set"}
# print(len(dd))
# print(dd.pop(1))
# print(dd.popitem())

# di = {i:i**3 for i in range(50, 60)}  # Generate.
# print(di)
