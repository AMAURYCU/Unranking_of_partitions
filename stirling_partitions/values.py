# Auto-generated placeholder
"""numbers module (placeholder)

Utilities for numeric helpers for unranking algorithms.
"""
import functools
from math import factorial

def numbers_info():
    """Return a short description."""
    return "numbers module placeholder"


if __name__ == "__main__":
    print(numbers_info())

@functools.lru_cache(maxsize=None)
def s2(n, k):
    if (n > 0 and k == 0) or k > n:
        return 0
    if n == k:
        return 1
    return k * s2(n - 1, k) + s2(n - 1, k - 1)


def formule2new(n, k, r, d0, d1):
    if d0 >= d1:
        return 0
    if d1 == 0:
        return s2(n,k)
    u = 0
    j = 0
    coefA = n - d0 - j
    coefB = n - d1 - j
    acc = 0
    while n-r-(u+1) >=0:
        acc += (coefA - coefB) * s2(n-r-u, k-1)
        u+=1
        j+=1
        coefA = (coefA * (n - d0 - j)) // (u + 1)
        coefB = (coefB * (n - d1 - j)) // (u + 1)

    return acc