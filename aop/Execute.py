from aop.Logger import *


class Execute:

    @before
    def exe1(self):
        print("exe1：execute")

    @after
    def exe2(self):
        print("exe2：execute")

    @arround
    def exe3(self):
        print("exe3：execute")

    @afterReturning
    def exe4(self):
        print("exe4：execute")

    @afterThrowing
    def exe5(self):
        print("exe3：execute")
        raise RuntimeError()
