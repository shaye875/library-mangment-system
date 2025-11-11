from Library.library import Library
from User.User import User
from Book.book import Book
from File.JsonFile import JsonFile
from File.csvfile import *

if __name__ == "__main__":

    library = Library()
    user = User("yossi", 2)
    book = Book("Harry potter", "JK rolling", 1234)

    library.add_user(user)
    library.add_book(book)

    user.add_book(book)

    JsonFile.write("users.json", library.users)
    Csvfile.write(library.users)




