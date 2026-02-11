# Auto-generated placeholder
"""numbers module (placeholder)

Utilities for numeric helpers for unranking algorithms.
"""
import functools
import math
def numbers_info():
    """Return a short description."""
    return "numbers module placeholder"


if __name__ == "__main__":
    print(numbers_info())


@functools.lru_cache(maxsize=None)
def count_lah_part(n,k):
    if k == 0: 
        return 1 if n == 0 else 0
    if k>n or n < 0: 
        return 0 
    return count_lah_part(n-1,k-1)+(n-1+k)*count_lah_part(n-1,k)

for n in range(1000):
    print(count_lah_part(n, int(math.sqrt(n))))