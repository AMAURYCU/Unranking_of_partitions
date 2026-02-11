import functools 



@functools.lru_cache(maxsize=None)
def count_lah_part(n,k):
    if k == 0: 
        return 1 if n == 0 else 0
    if k>n or n < 0: 
        return 0 
    return count_lah_part(n-1,k-1)+(n-1+k)*count_lah_part(n-1,k)


def count_lah_part_inf_k(n,k):
    return sum(count_lah_part(n,i) for i in range(0,k+1))


