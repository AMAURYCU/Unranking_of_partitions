# Auto-generated placeholder
"""combinatorial module (placeholder)

Utilities for combinatorial helpers for unranking algorithms.
"""

from  values import count_lah_part

def combinatorial_info():
    """Return a short description."""
    return "combinatorial module placeholder"


if __name__ == "__main__":
    print(combinatorial_info())


def unrank_lah_partition(n,k,r):
    if k == 0: 
        return []
    if n == 0: 
        return []
    if r < (n-1+k)*count_lah_part(n-1,k):
        pos, r = divmod(r, count_lah_part(n-1,k))
        part = unrank_lah_partition(n-1,k,r)
        for l in part: 
            pos = pos-len(l)-1
            if pos < 0:
                pos = len(l)+1+pos
                l.insert(pos,n)
                break 
        return part 
    r -= (n-1+k)*count_lah_part(n-1,k)
    
    part = unrank_lah_partition(n-1,k-1,r)
    part.append([n])
    return part