def basic_decorator(fn):
    def wrapper():
        print("start wrapper")
        fn()
        print("end wrapper")

    return wrapper


@basic_decorator
def say_hello():
    print("Hello")


say_hello()
