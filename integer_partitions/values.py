# Auto-generated placeholder
"""numbers module (placeholder)

Utilities for numeric helpers for unranking algorithms.
"""

import functools

def numbers_info():
    """Return a short description."""
    return "numbers module placeholder"


if __name__ == "__main__":
    print(numbers_info())

@functools.lru_cache(maxsize=None)
def count_integer_part(n,k):
    if k == 0: 
        return 0 if n > 0 else 1
    if n  == 0:
        return 0 if k > 0 else 1
    if n < k :
        return 0 
    if n == k :
        return 1 
    return count_integer_part(n-1,k-1) + count_integer_part(n-k,k)

