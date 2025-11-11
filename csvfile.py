class Csvfile:
    @staticmethod
    def write(books):
        name = input("what file name\n")
        str = ""
        for book in books:
            str += book.__str__()
            str += '\n'
        with open(f'{name}.csv','w') as f:
            f.write(str)
    @staticmethod
    def read(file):
        with open(file,'r') as f:
            print(f.read())

