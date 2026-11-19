from time import perf_counter
from turtle import st


def apply_discount(discount_percent):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * (1 - discount_percent / 100)

        return wrapper

    return decorator


def add_tax(tax_percent):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * (1 + tax_percent / 100)

        return wrapper

    return decorator


@add_tax(27)
@apply_discount(10)
def summa_price(a, b):
    return a + b


print(summa_price(10, 10))


def performance(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        end = perf_counter()
        print(f"{(end - start):.10f}")

    return wrapper


@performance
def log():
    print("hello")


log()
