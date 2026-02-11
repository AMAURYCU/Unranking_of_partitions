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
def count_ordered_lah_rec(n,k):
    if k == 0 and n == 0:
        return 1 
    if (k == 0 and n != 0) or (k>n)or n<0:
        return 0 
    return (n-1+k)*count_ordered_lah_rec(n-1,k)+ k*count_ordered_lah_rec(n-1,k-1)
