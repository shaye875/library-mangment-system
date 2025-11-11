from book import *
from User import *
class Csvfile:
    @staticmethod
    def write(books_or_user):
        name = input("what file name\n")
        str = ""
        for book in books_or_user:
            str += book.__str__()
            str += '\n'
        with open(f'{name}.csv','w') as f:
            f.write(str)
    @staticmethod
    def read(file):
        with open(file,'r') as f:
            print(f.read())

