import pickle

class Book:
    def __init__(self):
        self.pages = []
    def add_page(self, text):
        self.pages.append(f'Page: {len(self.pages) + 1} - {text}')
    def __iter__(self):
        return iter(self.pages)
... 
...     
>>> book = Book()
>>> for i in range(1, 8):
...     book.add_page(f'the page number is {i}')
... 
...     
>>> for page in book:
...     print(page)
... 
...     
Page: 1 - the page number is 1
Page: 2 - the page number is 2
Page: 3 - the page number is 3
Page: 4 - the page number is 4
Page: 5 - the page number is 5
Page: 6 - the page number is 6
Page: 7 - the page number is 7
>>> 
>>> 
>>> with open('data.pickle', 'wb') as fo:
...     pickle.dump(book, fo)
... 
...     
>>> with open('data.pickle', 'rb') as fo:
...     data_new_book = pickle.load(fo)
... 
...     
>>> for page in data_new_book:
...     print(page)
... 
...     
Page: 1 - the page number is 1
Page: 2 - the page number is 2
Page: 3 - the page number is 3
Page: 4 - the page number is 4
Page: 5 - the page number is 5
Page: 6 - the page number is 6
Page: 7 - the page number is 7
