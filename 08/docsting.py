# int, float, bool, str, tuple[str, str, int], list[int], dict, None...
# datetime, date, time
# union: str | None

# use Google style guide (or maybe numpy)
def summa(a: int, b: int) -> int:
    """
    Summa two int number

    Args:
        a: The first int value.
        b: The second int value.

    Returns:
        The sum value ot the two integers.
    """
    return a + b


# print(summa("10", "20"))
print(summa(10, 10))
