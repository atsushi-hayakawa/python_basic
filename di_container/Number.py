from abc import *


class Number(metaclass=ABCMeta):

    @abstractmethod
    def SayHello(self):
        pass
