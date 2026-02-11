# Auto-generated placeholder
"""combinatorial module (placeholder)

Utilities for combinatorial helpers for unranking algorithms.
"""

from values import s2 as stirling 

def combinatorial_info():
    """Return a short description."""
    return "combinatorial module placeholder"


if __name__ == "__main__":
    print(combinatorial_info())


def unrank_set_partition(n,k,r):
    if k == 0:
        return []
    if n == 0:
        return []
    if r < stirling(n-1,k-1):
        part = unrank_set_partition(n-1,k-1,r)
        part.append([n])
        return part 
    r -= stirling(n-1,k-1)
    pos, r = divmod(r, stirling(n-1,k))
    part = unrank_set_partition(n-1,k,r)
    part[pos].append(n)
    return part
