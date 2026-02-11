

from values import s2 as stirling 



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
