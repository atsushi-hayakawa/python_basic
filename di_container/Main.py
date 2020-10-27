from InstanceMaker import *


def main():
    print("main_start")
    for i in range(10):
        number = InstanceMaker(i).getInstance()
        print(str(i))
        number.SayHello()


main()
