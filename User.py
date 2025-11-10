
class User:

    def __init__(self, name, user_id, borrowed_books=None):
        self.__borrowed_books = [] if borrowed_books is None else borrowed_books
        self.__name = name
        self.__user_id = user_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books.copy()

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.user_id

    def set_borrowed_books(self, books):
        self.__borrowed_books = books

    def set_name(self, name):
        self.__name = name

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def add_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

