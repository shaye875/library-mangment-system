from Library.library import Library
from User.User import User
from Book.book import Book
from File.JsonFile import JsonFile
from File.csvfile import *

if __name__ == "__main__":

    library = Library()
    user = User("yossi", 2)
    user1 = User("avi",2345)
    book = Book("Harry potter 1", "JK rolling", 1234)
    book1 = Book('Harry potter 2','JK rolling',234)
    book2 = Book('Harry potter 3','JK rolling',5678)

    library.add_user(user)
    library.add_user(user1)
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book(user.user_id,book.isbn)
    library.return_book(user.user_id,book.isbn)
    print(library.name_available_books())
    library.borrow_book(2,234)
    JsonFile.write("users.json", library.users)
    print(JsonFile.read("users.json"))
    Csvfile.write(library.books,'books')
    Csvfile.read('books.csv')
    Csvfile.write(library.users,'users')
    Csvfile.read('users.csv')





