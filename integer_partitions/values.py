
import functools




@functools.lru_cache(maxsize=None)
def count_integer_part(n,k):
    if k == 0: 
        return 0 if n > 0 else 1
    if n  == 0:
        return 0 if k > 0 else 1
    if n < k :
        return 0 
    if n == k :
        return 1 
    return count_integer_part(n-1,k-1) + count_integer_part(n-k,k)

