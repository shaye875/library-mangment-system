from library import Library
from User import User
from book import Book
from JsonFile import JsonFile
from csvfile import *
if __name__ == "__main__":

    library = Library()
    user = User("yossi", 2)
    book = Book("Harry potter", "JK rolling", 1234)

    library.add_user(user)
    library.add_book(book)

    user.add_book(book)


    JsonFile.write("users.json", library.users)
    Csvfile.write(library.users)




