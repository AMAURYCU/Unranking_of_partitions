import functools




@functools.lru_cache(maxsize=None)
def s2(n, k):
    if (n > 0 and k == 0) or k > n:
        return 0
    if n == k:
        return 1
    return k * s2(n - 1, k) + s2(n - 1, k - 1)

@functools.lru_cache(maxsize=None)
def Bs2(n,k):
    if n == 0:
        return 1
    return sum([s2(n, i) for i in range(1, k+1)])


def formule2new(n, k,r, d0, d1):
    if d0 >= d1:
        return 0
    if d1 == 1:
        return Bs2(n,k)
    u = 0
    coefA = n - d0
    coefB = n - d1
    acc = 0
    while n-r-u >=0:
        acc += (coefA - coefB) * Bs2(n-r-u,k-1)
        u+=1
        coefA = (coefA * (n - d0 - u)) // (u + 1)
        coefB = (coefB * (n - d1 - u)) // (u + 1)

    return acc