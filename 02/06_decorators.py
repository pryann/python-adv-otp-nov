def basic_decorator(fn):
    def wrapper():
        print("start wrapper")
        fn()
        print("end wrapper")

    return wrapper


def say_hello():
    print("Hello")


# result = basic_decorator(say_hello)
# result()

basic_decorator(say_hello)()
