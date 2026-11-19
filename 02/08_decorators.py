def basic_decorator(fn):
    def wrapper(name):
        print("start wrapper")
        fn(name)
        print("end wrapper")

    return wrapper


@basic_decorator
def say_hello(name):
    print(f"Hello {name}")


say_hello("John")
