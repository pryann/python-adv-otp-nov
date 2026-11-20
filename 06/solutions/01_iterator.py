"""1. feladat: egy iterátor elfogyasztása."""


def main():
    iterator = iter(["piros", "zöld", "kék"])

    print(next(iterator))
    print(next(iterator))

    # A ciklus az iterátor következő elemétől folytatja a bejárást.
    for color in iterator:
        print(color)

    print(next(iterator, "elfogyott"))


if __name__ == "__main__":
    main()
