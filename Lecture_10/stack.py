# stack = []
# def push(value):
#     stack.append(value)
#
#
# def pop():
#     stack.pop()
#
#
# push(1)
# push(2)
# push(3)
# push(4)
# print(stack)
# pop()
# print(stack)
# pop()
# print(stack)
# pop()
# print(stack)


# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         self.stack.pop()
#
#
# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# print(s1.stack)
# s2 = Stack()
# print(s2.stack)
# s1.pop()
# print(s1.stack)


# class Stack:
#     def __init__(self):
#         self.__stack = []
#     def push(self, value):
#         self.__stack.append(value)
#     def pop(self):
#         try:
#             self.__stack.pop()
#         except:
#             return "NE OK"
#         return "OK"
#     def show(self):
#         return self.__stack
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         super().__init__()
#         self.counter = 0
#         self.summa = 0
#     def push(self, value):
#         self.counter += 1
#         self.summa += value
#         super().push(value)
#
#
# s1 = CountingStack()
# print(s1.show())
# print(s1.pop())
# print(s1.counter)
# print(s1.summa)
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# print(s1.show())
# print(s1.counter)
# print(s1.summa)
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())


# class Stack:
#     def __init__(self):
#         self.__stack = []
#     def push(self, value):
#         self.__stack.append(value)
#     def pop(self):
#         try:
#             self.__stack.pop()
#         except:
#             return "NE OK"
#         return "OK"
#     def show(self):
#         return self.__stack
#
#
# s1 = Stack()
# print(s1.pop())
# s1.push(123)
# s1.push(1)
# s1.push(2)
# print(s1.show())
# print(s1.pop())
# print(s1.show())
