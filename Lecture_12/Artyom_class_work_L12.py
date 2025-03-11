print(1, 2, 3)
1 2 3
print(22)
22
def Pront(values):
    for val in vals:
        print(val, end=" ")
    print()

    
Pront([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Pront([1, 2, 3, 4])
  File "<pyshell#7>", line 2, in Pront
    for val in vals:
NameError: name 'vals' is not defined. Did you mean: 'vars'?
def Pront(values):
    for val in values:
        print(val, end=" ")
    print()

    
Pront([1, 2, 3, 4])
1 2 3 4 
Pront("dfsthgs")
d f s t h g s 
Pront(1, 2, 3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Pront(1, 2, 3, 4, 5)
TypeError: Pront() takes 1 positional argument but 5 were given
print(1, 2, 3, 4)
1 2 3 4
def Pront(*values):
    print(type(values))
    
    for val in values:
        print(val, end=" ")
    print()

    
Pront(1, 2, 3, 4, 5)
<class 'tuple'>
1 2 3 4 5 
Pront(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")
<class 'tuple'>
1 2 3 4 5 [1, 2, 3, 4] sadgfs 
print(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")
1 2 3 4 5 [1, 2, 3, 4] sadgfs
def Pront(*args):
    print(type(args))
    
    for val in args:
        print(val, end=" ")
    print()

    
Pront(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")
<class 'tuple'>
1 2 3 4 5 [1, 2, 3, 4] sadgfs 
a, b, *c = [1, 2, 3, 4, 5]
c
[3, 4, 5]
def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, sep = sep1)
    print(end = end1)

    
Pront(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")
1
2
3
4
5
[1, 2, 3, 4]
sadgfs

def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, sep = sep1, end="")
    print(end = end1)

    
Pront(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")
12345[1, 2, 3, 4]sadgfs
def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, end = sep1)
    print(end = end1)

    
Pront(1, 2, 3, 4, 5, [1, 2, 3, 4], "sadgfs")

1 2 3 4 5 [1, 2, 3, 4] sadgfs 



def balances(**balance):
    print(balance)
    print(type(balance))
    for k, w in balance.items():
        print("\t", k, ":", w)
    print()

    
balances(1,2,3,4,4)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    balances(1,2,3,4,4)
TypeError: balances() takes 0 positional arguments but 5 were given
balances(name="Vasia", cash=120000)
{'name': 'Vasia', 'cash': 120000}
<class 'dict'>
	 name : Vasia
	 cash : 120000

def numbers(name="Joe", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Joe
()
{}
def numbers(name="Joe", args, kwargs):
    print(name)
    print(args)
    print(kwargs)
    
SyntaxError: parameter without a default follows parameter with a default
def numbers(args, kwargs, name="Joe"):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    numbers()
TypeError: numbers() missing 2 required positional arguments: 'args' and 'kwargs'
def numbers(name="Joe", *args, **kwargs, ):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Joe
()
{}
numbers("Vasia", 1,2,3,44,5,6,7,8,"stfhdty", age=100, apples=99)
Vasia
(1, 2, 3, 44, 5, 6, 7, 8, 'stfhdty')
{'age': 100, 'apples': 99}
def numbers(name="Joe", **kwargs, *args, ):
    print(name)
    print(args)
    print(kwargs)
    
SyntaxError: arguments cannot follow var-keyword argument
def numbers(*args, **kwargs, name="Joe"):
    print(name)
    print(args)
    print(kwargs)
    
SyntaxError: arguments cannot follow var-keyword argument
def numbers(name="Joe", *args, **kwargs, ):
    print(name)
    print(args)
    print(kwargs)

    
def num_sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)

    
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
{}
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    numbers(1,2,3,4,5,6)
  File "<pyshell#72>", line 4, in numbers
    num_sum(args)
  File "<pyshell#69>", line 4, in num_sum
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def num_sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)

    
numbers(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
{}
((1, 2, 3, 4, 5, 6),)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    numbers(1,2,3,4,5,6)
  File "<pyshell#72>", line 4, in numbers
    num_sum(args)
  File "<pyshell#75>", line 5, in num_sum
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    num_sum(*args)

    
numbers(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
{}
(1, 2, 3, 4, 5, 6)
21
li1, li2 = [1,2,3], [4,5,6]
li1
[1, 2, 3]
li2
[4, 5, 6]
li3 = li1+li2
li3
[1, 2, 3, 4, 5, 6]
li3=[li1, li2]
li3
[[1, 2, 3], [4, 5, 6]]
li3=[*li1, *li2]
li3
[1, 2, 3, 4, 5, 6]
st="khfhddhj"
li = [st]
li
['khfhddhj']
li = [*st]
li
['k', 'h', 'f', 'h', 'd', 'd', 'h', 'j']
di = {"1":2, "2":3}
di1 = {"11":22, "22":33}
di3 = {**di, **di1}
di3
{'1': 2, '2': 3, '11': 22, '22': 33}
*ttt, = "kjgjgdfjmn"
ttt
['k', 'j', 'g', 'j', 'g', 'd', 'f', 'j', 'm', 'n']
a, *ttt = "kjgjgdfjmn"
ф
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    ф
NameError: name 'ф' is not defined
a
'k'
ttt
['j', 'g', 'j', 'g', 'd', 'f', 'j', 'm', 'n']
*ttt, = "kjgjgdfjmn"
ttt
['k', 'j', 'g', 'j', 'g', 'd', 'f', 'j', 'm', 'n']


# b^2-4ac
def D(b, a, c):
    return b**2 - 4*a*c

D
<function D at 0x1056d22a0>
#def cond (z,x,y, b,a,c):)

lambda: 2
<function <lambda> at 0x1056d3240>
def retTwo:
    
SyntaxError: expected '('
def retTwo():
    return 2

(lambda: 2)()
2
(lambda: 2)
<function <lambda> at 0x1056d3240>
(lambda: 2)()
2
lambda a,b,c: a*b-c
<function <lambda> at 0x1056d3100>
(lambda a,b,c: a*b-c)
<function <lambda> at 0x1056d3420>
(lambda a,b,c: a*b-c)()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    (lambda a,b,c: a*b-c)()
TypeError: <lambda>() missing 3 required positional arguments: 'a', 'b', and 'c'
(lambda a,b,c: a*b-c)(2,3,4)
2
def cond(z,x,y, b,a,c):
    return z+x+y + (lambda b,a,c: b**2 - 4*a*c)(b,a,c)

cond(1,2,3, 4,3,5)
-38


li = [2,3,4,5,7]
for i in li:
    print(i)

    
2
3
4
5
7
li_iter = iter(li)
li_iter
<list_iterator object at 0x1056d82b0>
next(li_iter)
2
next(li_iter)
3
next(li_iter)
4
next(li_iter)
5
next(li_iter)
7
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    next(li_iter)
StopIteration
st = 'jhfhfst'
st_iter = iter(st)
st_iter
<str_ascii_iterator object at 0x1056d89a0>
next(st_iter)
'j'
next(st_iter)
'h'
next(st_iter)
'f'
next(st_iter)
'h'
next(st_iter)
'f'
next(st_iter)
's'
next(st_iter)
't'
next(st_iter)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    next(st_iter)
StopIteration



class PowFive:
    def __init(self, maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 0
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration

    
p = PowFiwe(15)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    p = PowFiwe(15)
NameError: name 'PowFiwe' is not defined. Did you mean: 'PowFive'?
p = PoWFive(15)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    p = PoWFive(15)
NameError: name 'PoWFive' is not defined. Did you mean: 'PowFive'?
p = PowFive(15)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    p = PowFive(15)
TypeError: PowFive() takes no arguments
p = PowFive(15)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    p = PowFive(15)
TypeError: PowFive() takes no arguments
class PowFive:
    def __init(self, maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration

    
p = PowFive(4)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    p = PowFive(4)
TypeError: PowFive() takes no arguments
class PowFive:
    def __init__(self, maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration

    
p = PowFive(4)
p
<__main__.PowFive object at 0x10506aba0>
p_iter = p.iter()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    p_iter = p.iter()
AttributeError: 'PowFive' object has no attribute 'iter'
for i in p:
    print(i)

    
5
25
125
625
li = [0,1,4,9,16,25,36,49,64,81]
gen=(i**2 for i in range(10))
gen
<generator object <genexpr> at 0x10563fe00>
gen()
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    gen()
TypeError: 'generator' object is not callable
for val in gen:
    print(val)

    
0
1
4
9
16
25
36
49
64
81
for val in gen:
    print(val)

    
for val in gen:
    print(val)

    
gen = (i**2 for i in range (10))
next(gen)
0
next(gen)
1
next(gen)
4
next(gen)
9
next(gen)
16
next(gen)
25
next(gen)
36
next(gen)
49
next(gen)
64
next(gen)
81
next(gen)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    next(gen)
StopIteration


gen = (i**2 for i in range(10))

li = [i**2 for i in gen]
li
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
next(gen)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    next(gen)
StopIteration




def retNumbers(n):
    for i in range(n):
        return i

retNumbers(5)
0
def retNumbers(n):
    for i in range(n):
        yield i**2

        
r = retNumbers(5)
r
<generator object retNumbers at 0x10563fd30>
next(r)
0
next(r)
1
next(r)
4
next(r)
9
next(r)
16
next(r)
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    next(r)
StopIteration
for i in retNumbers(10):
    print(i)

    
0
1
4
9
16
25
36
49
64
81



def mulFive(n):
    return n*5

li = [1,2,3,4]
res_li = list(map(mulFive, li))
res_li
[5, 10, 15, 20]


def a():
    x = 10

    
def a():
    x = 10
    def inner(number):
        return number**x
    return inner

res = a()
res
<function a.<locals>.inner at 0x1056e0e00>
res(6)
60466176


def numPowTwo():
    num = 0
    def inner():
        nonlocal num
        num **= 2
        return num
    return inner

res = numPowTwo()
res
<function numPowTwo.<locals>.inner at 0x1056e91c0>
res()
0
res()
0
def numPowTwo():
    num = 2
    def inner():
        nonlocal num
        num **= 2
        return num
    return inner

res = numPowTwo()
res()
4
res()
16
res()
256
res()
65536
res()
4294967296
res()
18446744073709551616
res()
340282366920938463463374607431768211456
res()
115792089237316195423570985008687907853269984665640564039457584007913129639936
res()
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096
res()
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
res()
32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230656
res()
1044388881413152506691752710716624382579964249047383780384233483283953907971557456848826811934997558340890106714439262837987573438185793607263236087851365277945956976543709998340361590134383718314428070011855946226376318839397712745672334684344586617496807908705803704071284048740118609114467977783598029006686938976881787785946905630190260940599579453432823469303026696443059025015972399867714215541693835559885291486318237914434496734087811872639496475100189041349008417061675093668333850551032972088269550769983616369411933015213796825837188091833656751221318492846368125550225998300412344784862595674492194617023806505913245610825731835380087608622102834270197698202313169017678006675195485079921636419370285375124784014907159135459982790513399611551794271106831134090584272884279791554849782954323534517065223269061394905987693002122963395687782878948440616007412945674919823050571642377154816321380631045902916136926708342856440730447899971901781465763473223850267253059899795996090799469201774624817718449867455659250178329070473119433165550807568221846571746373296884912819520317457002440926616910874148385078411929804522981857338977648103126085903001302413467189726673216491511131602920781738033436090243804708340403154190336
res()

res()
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    res()
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
import sys

class Dog:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
type(Dog)
<class 'type'>
isinstance(d, Dog)
True
isinstance(Dog, type)
True
isinstance(int, type)
True
isinstance(list, type)
True
list.__bases__
(<class 'object'>,)
isinstance(list, type)
True


class Number:
    Num = 99
    def get_number(self):
        return 55

    
n = Number()
n.Num
99
n.get_number
<bound method Number.get_number of <__main__.Number object at 0x10506ae40>>
n.get_number()
55


NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
NameError: name 'get_number' is not defined. Did you mean: 'retNumbers'?
>>> nn = NumberFromType()
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    nn = NumberFromType()
NameError: name 'NumberFromType' is not defined
>>> NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
NameError: name 'get_number' is not defined. Did you mean: 'retNumbers'?
>>> NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JoJo"})
NameError: name 'get_number' is not defined. Did you mean: 'retNumbers'?
>>> 
>>> 
>>> class Number:
...     Num = 99
...     def get_number(self):
...         return 55
... 
...     
>>> name = input()
Car
>>> name
'Car'
>>> di={"VIN":123456, "BodyType":"Sedan", "Counter":0}
>>> new_user_type = type(name, (object,), di)
>>> new_user_type
<class '__main__.Car'>
>>> my_car = new_user_type()
