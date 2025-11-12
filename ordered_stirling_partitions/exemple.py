"""Exemple d'utilisation pour ordered_stirling_partitions."""

from . import numbers, combinatorial, lexicographic


def main():
    print("numbers:", numbers.numbers_info())
    print("combinatorial:", combinatorial.combinatorial_info())
    print("lexicographic:", lexicographic.lexicographic_info())


if __name__ == "__main__":
    main()
