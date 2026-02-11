from values import count_integer_part


def rev_lex_rev_can(n,k,r):
    if k == 1: 
        return [n]

    init = [1] * k
    if n == k :
        return init 
    for j in range(1,k+1):
        if r < count_integer_part(n - k, j):
            res = rev_lex_rev_can(n - k, j, r)
            for i in range(len(res)):
                init[i] += res[i]
            return init 
        r -= count_integer_part(n - k, j)
    return init