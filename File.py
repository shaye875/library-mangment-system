from abc import ABC, abstractmethod


class File(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

