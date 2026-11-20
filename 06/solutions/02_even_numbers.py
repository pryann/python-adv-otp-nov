"""2. feladat: páros számok előállítása generátorral."""


def even_numbers(limit):
    """Előállítja a páros számokat nullától a határig, azt is beleértve."""
    for number in range(0, limit + 1, 2):
        yield number


def main():
    print(list(even_numbers(6)))
    print(list(even_numbers(5)))

    numbers = even_numbers(6)
    print(next(numbers))
    print(next(numbers))


if __name__ == "__main__":
    main()
