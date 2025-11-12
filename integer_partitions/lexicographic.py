# Auto-generated placeholder
"""lexicographic module (placeholder)

Utilities for lexicographic ordering helpers for unranking algorithms.
"""

from  numbers import count_integer_part

def lexicographic_info():
    """Return a short description."""
    return "lexicographic module placeholder"


if __name__ == "__main__":
    print(lexicographic_info())

def lex_unrank_part_pref(n,k,r):
    acc = []
    lem = 2
    if k == n: 
        return [1] * k
    if k == 1:
        return [n]
    if r < count_integer_part(n-1,k-1):
        acc = [1]
        lem = 1 
        n -= 1 
        k-= 1
    else:
        r = r -  count_integer_part(n-1,k-1)
    for _ in range(1,k+1):
        if k == 1:
                acc.append(n)
                return acc 
        for j in range(lem, n-k+1):
            magic = count_integer_part(n-j-(k-1)*(j-1),k-1)
            if r < magic:
                acc.append(j)
                n -= j 
                k -= 1 
                lem = j 
                break 
            r -= magic
    return acc 