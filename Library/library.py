from Book.book import *

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)


    def add_user(self,user):
        self.users.append(user)

    def borrow_book(self,user_id,book_isbn):
        bol = True
        for book in self.books:
            if book.isbn == book_isbn:
                for user in self.users:
                    if user.user_id == user_id:
                        user.add_book(book)
                        book.set_is_available(False)
                        bol = False
                        break
            if bol == False:
                break

    def return_book(self,user_id,book_isbn):
        bol = True
        for book in self.books:
            if book.isbn == book_isbn:
                for user in self.users:
                    if user.user_id == user_id:
                        user.return_book(book)
                        book.set_is_available(True)
                        bol = False
                        break
            if bol == False:
                break

    def list_available_books(self):
        available = []
        for book in self.books:
            if book.is_available == True:
                available.append(book)
        return available

    def name_available_books(self):
        available = []
        for book in self.books:
            if book.is_available == True:
                available.append(book.title)
        return available

    def search_book_by_title(self,title):
        for book in self.books:
            if book.title == title:
                return book

    def search_book_by_author(self,author):
        for book in self.books:
            if book.author == author:
                return book










