# Auto-generated placeholder
"""combinatorial module (placeholder)

Utilities for combinatorial helpers for unranking algorithms.
"""

import values

def combinatorial_info():
    """Return a short description."""
    return "combinatorial module placeholder"


if __name__ == "__main__":
    print(combinatorial_info())

def unrank_ordered_partition(n,k,r):
    if k == 0:
        return []
    if n == 0:
        return []
    if r < k* values.os2(n-1,k-1):
        pos,r = divmod(r, values.os2(n-1,k-1))
        part = unrank_ordered_partition(n-1, k-1, r)
        part= part[:pos] + [[n]] + part[pos:]
        return part
    r -= k* values.os2(n-1,k-1)
    pos, r = divmod(r, values.os2(n-1, k))
    part = unrank_ordered_partition(n-1, k, r)
    part[pos].append(n)
    return part