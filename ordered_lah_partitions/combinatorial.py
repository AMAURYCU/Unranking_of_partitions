

from   values import count_ordered_lah_rec as ordered_lah_rec






def unrank_ordered_lah_partition(n,k,r):
    if k == 0: 
        return []
    if n == 0: 
        return []
    if r < (n-1+k)*ordered_lah_rec(n-1,k):
        pos, r = divmod(r, ordered_lah_rec(n-1,k))
        part = unrank_ordered_lah_partition(n-1,k,r)
        for l in part: 
            pos = pos-len(l)-1
            if pos < 0:
                pos = len(l)+1+pos
                l.insert(pos,n)
                break 
        return part 
    r -= (n-1+k)*ordered_lah_rec(n-1,k)
    pos,r = divmod(r, ordered_lah_rec(n-1,k-1))
    part = unrank_ordered_lah_partition(n-1,k-1,r)
    part.insert(pos,[n])
    return part