import inspect


def main():
    print("main実行")
    mod = __import__("SampleClass", fromlist=["reflection.SampleClass"])
    class_def = getattr(mod, "SampleClass")
    obj = class_def()
    obj.shout()

    print(inspect.getmembers(obj, inspect.ismethod)[0][0])


main()
