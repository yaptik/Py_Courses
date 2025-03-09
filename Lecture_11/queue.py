class Empty(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'Empty: message: {self.message}'

    
raise Empty('Очередь пустая')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise Empty('Очередь пустая')
Empty: Empty: message: Очередь пустая
try:
    raise Empty('Очередь пустая')
except Empty as e:
    print(e)

    
Empty: message: Очередь пустая
class Queue:
    def __init__(self):
        self.__queue = []
    def get(self):
        if len(self.__queue) < 1:
            raise Empty('Очередь пустая')
        return sef.__queue.pop(0)

    
class Queue:
    def __init__(self):
        self.__queue = []
    def get(self):
        if len(self.__queue) < 1:
            raise Empty('Очередь пустая')
        return sef.__queue.pop(0)
    def put(self, val):
        self.__queue.append(val)

        
q1 = Queue()
q1.put(1)
q1.put(2)
q1.put(5)
q1.put(55)
q1.get()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    q1.get()
  File "<pyshell#19>", line 7, in get
    return sef.__queue.pop(0)
NameError: name 'sef' is not defined. Did you mean: 'self'?
>>> q1.get()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    q1.get()
  File "<pyshell#19>", line 7, in get
    return sef.__queue.pop(0)
NameError: name 'sef' is not defined. Did you mean: 'self'?
>>> q1
<__main__.Queue object at 0x0000010B6120D610>
>>> print(q1)
<__main__.Queue object at 0x0000010B6120D610>
>>> class Empty(Exception):
...     def __init__(self, message):
...         self.message = message
...     def __str__(self):
...         return f'Empty: message: {self.message}'
... 
...     
>>> class Queue:
...     def __init__(self):
...         self.__queue = []
...     def get(self):
...         if len(self.__queue) < 1:
...             raise Empty('Очередь пустая')
...         return sef.__queue.pop(0)
...     def put(self, val):
...         self.__queue.append(val)
... 
...         
>>> q1 = Queue()
>>> q1.put(1)
>>> q1.put(2)
>>> q1.put(5)
>>> q1.put(55)
>>> q1.get()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    q1.get()
  File "<pyshell#32>", line 7, in get
    return sef.__queue.pop(0)
NameError: name 'sef' is not defined. Did you mean: 'self'?
>>> class Queue:
...     def __init__(self):
...         self.__queue = []
...     def get(self):
...         if len(self.__queue) < 1:
...             raise Empty('Очередь пустая')
...         return self.__queue.pop(0)
...     def put(self, val):
...         self.__queue.append(val)
... 
...         
>>> q1 = Queue()
>>> q1.put(1)
>>> q1.put(2)
>>> q1.put(5)
>>> q1.put(55)
>>> q1.get()
1
>>> q1.get()
2
>>> q1.get()
5
>>> q1.get()
55
>>> q1.get()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    q1.get()
  File "<pyshell#40>", line 6, in get
    raise Empty('Очередь пустая')
Empty: Empty: message: Очередь пустая
