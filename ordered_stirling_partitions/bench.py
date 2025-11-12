"""Micro-benchmarks for ordered_stirling_partitions.

Run with: python -m ordered_stirling_partitions.bench
"""

from timeit import timeit
from . import numbers, combinatorial, lexicographic


def bench(iterations: int = 10000):
    print("Benchmarks for ordered_stirling_partitions ({} iterations)".format(iterations))

    t_numbers = timeit("numbers.numbers_info()", globals={'numbers': numbers}, number=iterations)
    print(f"numbers.numbers_info: {t_numbers:.6f}s total, {t_numbers/iterations:.9f}s per call")

    t_comb = timeit("combinatorial.combinatorial_info()", globals={'combinatorial': combinatorial}, number=iterations)
    print(f"combinatorial.combinatorial_info: {t_comb:.6f}s total, {t_comb/iterations:.9f}s per call")

    t_lex = timeit("lexicographic.lexicographic_info()", globals={'lexicographic': lexicographic}, number=iterations)
    print(f"lexicographic.lexicographic_info: {t_lex:.6f}s total, {t_lex/iterations:.9f}s per call")


if __name__ == '__main__':
    bench(10000)
