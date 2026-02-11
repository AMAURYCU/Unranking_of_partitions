"""Exemple d'utilisation pour stirling_partitions."""

import combinatorial, lexicographic



# Auto-generated placeholder
"""lexicographic module (placeholder)

Utilities for lexicographic ordering helpers for unranking algorithms.
"""

from  values import *

def lexicographic_info():
    """Return a short description."""
    return "lexicographic module placeholder"


if __name__ == "__main__":
    print(lexicographic_info())

def permutation_unrank_lex(n, Pos):
    L = [i for i in range(1, n+1)]
    P = []
    for b in range(len(Pos)):
        p = []
        for i in Pos[b]:
            p.append(L[i])
            del L[i]
        P.append(p)
    return P



def unrankDicho(n, k, r):
    n0 = n
    Res = []
    while k > 1:
        A, acc = blockDicho(n, k, r)
        Res.append(A)
        r -= acc
        n -= len(A)
        k -= 1
    Res.append([0]*n)
    Res = permutation_unrank_lex(n0, Res)
    return Res



def blockDicho(n, k, r):

    ret = []
    acc = 0

    d0 = 0
    position = 1
    inf = 1
    sup = n
    complete = False
    while not complete:

        while inf < sup:
            mid = (inf + sup) // 2
          

            rankMid = formule2new(n, k, position, d0, mid) + acc
            if r >= rankMid:
                inf = mid + 1
            else:
                sup = mid

        mid = inf
        rankMid = formule2new(n, k, position, d0, mid -1) + acc
        ret.append(mid - position)
        acc = rankMid
        stirling = s2(n - position, k - 1)
        if r < stirling + acc:
            complete = True
        else:
            position += 1
            d0 = mid
            inf = d0+1
            sup = n
            acc = stirling + acc

    #print(ret)
    return ret, acc



