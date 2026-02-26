import functools
from math import factorial, comb
@functools.lru_cache(maxsize=None)
def lah(n,k):
    if n == 0 and k !=0:
        return 0
    if k ==1 : 
        return factorial(n)
    if k == n:
        return 1 
    return lah(n-1,k-1)+(n-1+k)*lah(n-1,k)
def ord_lah_inf_k(n,k):
    return sum(factorial(l)*lah(n,l)*comb(k,l) for l in range(0,k+1))



