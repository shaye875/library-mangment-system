class Book:
    def __init__(self,title,author,isbn,is_available=True):

        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = is_available

    @property
    def is_available(self):
        return self.__is_available

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    def set_is_available(self,type:bool):
        self.__is_available = type

    def __str__(self):
        return f"the title {self.__title} of {self.__author} the isbn is {self.__isbn} and this is available?:\n{self.__is_available}"