class MethodHolder:

    index = 0

    def InstanceMethod(self):
        self.index = self.index + 1
        print("Successful instance method call:" + str(self.index))

    @classmethod
    def ClassMethod(cls):
        cls.index = cls.index + 1
        print("Successful class method call:" + str(cls.index))

    @staticmethod
    def StaticMethod():
        MethodHolder.index = MethodHolder.index + 1
        print("Successful static method call:" + str(MethodHolder.index))


class MethodHolderExtended(MethodHolder):

    index = 100
