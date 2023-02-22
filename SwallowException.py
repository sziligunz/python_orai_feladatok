from functools import wraps


def swallow_exception(type):
    def inner(func):
        @wraps(func)
        def innerinner(*args, **kwargs):
            res = None
            try:
                res = func(*args, **kwargs)
            except type as e:
                print(e)
            return res
        return innerinner
    return inner


@swallow_exception(ZeroDivisionError)
def example(number):
    print(number)
    raise ZeroDivisionError("Some error message")


def example2(number):
    print(number)
    raise ZeroDivisionError("Some error message")


example(10)
example2(10)
