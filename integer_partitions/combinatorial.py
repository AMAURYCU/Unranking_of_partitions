# Auto-generated placeholder
"""combinatorial module (placeholder)

Utilities for combinatorial helpers for unranking algorithms.
"""

from  numbers import count_integer_part

def combinatorial_info():
    """Return a short description."""
    return "combinatorial module placeholder"


if __name__ == "__main__":
    print(combinatorial_info())


def unrank_integer_part(n,k,r):
    if k == 0: 
        return []
    if n == 1: 
        return [1]
    else: 
        if r < count_integer_part(n-1,k-1):
            return [1]+unrank_integer_part(n-1,k-1,r)
        else :
            
            part = unrank_integer_part(n-k,k,r-count_integer_part(n-1,k-1))
            return [r+1 for r in part]
  