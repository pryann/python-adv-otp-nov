def basic_decorator(fn):
    def wrapper(*args, **kwargs):
        print("start wrapper")
        fn(*args, **kwargs)
        print("end wrapper")

    return wrapper


@basic_decorator
def say_hello(name):
    print(f"Hello {name}")


@basic_decorator
def say_my_name(first_name, last_name):
    print(f"{first_name} {last_name}")


say_hello("John")
say_my_name("Jane", "Doe")
