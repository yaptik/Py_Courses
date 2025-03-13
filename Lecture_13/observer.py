class Sub:
    def react(self, creator):
        print('Sub реагирует лайком от:')
        print(creator)

...         
>>> class Creator:
...     def __init__(self, name):
...         self.subs = []
...         self.name = name
...     def __str__(self):
...         return f'{self.name}'
...     def follow(self, sub):
...         self.subs.append(sub)
...         print('подписчик подписался')
...     def noty(self):
...         for sub in self.subs:
...             sub.react(self)
...     def create_event(self):
...         print('новое видео')
...         self.noty()
... 
...         
>>> chan_owner = Creator('MGH Chan')
>>> chan_owner.subs
[]
>>> chan_owner.name
'MGH Chan'
>>> sub1 = Sub()
>>> sub2 = Sub()
>>> sub3 = Sub()
>>> chan_owner.follow(sub1)
подписчик подписался
>>> chan_owner.follow(sub2)
подписчик подписался
>>> chan_owner.subs
[<__main__.Sub object at 0x000001E7DBB25250>, <__main__.Sub object at 0x000001E7DC20D280>]
>>> chan_owner.create_event()
новое видео
Sub реагирует лайком от:
MGH Chan
Sub реагирует лайком от:
MGH Chan
