def before(func):
    def inner(*args, **kwargs):

        print(func.__name__ + "：Start")

        result = func(*args, **kwargs)

        return result

    return inner


def after(func):
    def inner(*args, **kwargs):

        result = func(*args, **kwargs)

        print(func.__name__ + "：End")

        return result

    return inner


def arround(func):
    def inner(*args, **kwargs):

        print(func.__name__ + "：Start>>>>>>>>>>>>>>>>>>>>>>>>")

        result = func(*args, **kwargs)

        print(func.__name__ + "：End<<<<<<<<<<<<<<<<<<<<<<<<")

        return result

    return inner


def afterReturning(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(func.__name__ + "：Success")
            return result
        except RuntimeError:
            pass

    return inner


def afterThrowing(func):
    def inner(*args, **kwargs):

        try:
            result = func(*args, **kwargs)
            return result
        except RuntimeError:
            print(func.__name__ + "：fail")

    return inner
