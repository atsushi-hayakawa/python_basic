from di_container.EvenNumber import EvenNumber
from di_container.OddNumber import OddNumber


class InstanceMaker:

    index = 0

    def __init__(self, index):
        self.index = index

    def getInstance(self):
        if self.index % 2 == 0:
            return EvenNumber()
        else:
            return OddNumber()
