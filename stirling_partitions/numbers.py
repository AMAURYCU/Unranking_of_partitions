# Auto-generated placeholder
"""numbers module (placeholder)

Utilities for numeric helpers for unranking algorithms.
"""

def numbers_info():
    """Return a short description."""
    return "numbers module placeholder"


import functools    
@functools.lru_cache(maxsize=None)
def stirling(n,k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling(n-1,k) + stirling(n-1,k-1)

if __name__ == "__main__":
    print(numbers_info())
