"""3. feladat: az összes szín és méret párosítása."""

from itertools import product


def main():
    colors = ["piros", "kék"]
    sizes = ["S", "M"]

    variants = list(product(colors, sizes))
    print(variants)


if __name__ == "__main__":
    main()
