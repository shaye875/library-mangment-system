from book import *
from User import *
class Csvfile:
    @staticmethod
    def write(books_or_user):
        name = input("what file name\n")
        str = ""
        if books_or_user is Book:
         for book in books_or_user:
            str += book.__str__()
            str += '\n'
         with open(f'{name}.csv','w') as f:
            f.write(str)
        if books_or_user is User:
            for user in books_or_user:
                str += user
                str += '\n'
        with open(f'{name}.csv','w') as f:
            f.write(str)
    @staticmethod
    def read(file):
        with open(file,'r') as f:
            print(f.read())

