"""Exemple d'utilisation pour ordered_stirling_partitions."""

import combinatorial, lexicographic, values

def random_partition(n,k):
    import random
    rank = random.randint(0, values.os2(n,k)-1)
    return lexicographic.unrankDicho(n, k, rank)

def exhaust_gen_lex(n,k):
    res = []
    for r in range(values.os2(n,k)):
        res.append(lexicographic.unrankDicho(n, k, r))
    return res


def exhaust_gen_combinatorial(n,k):
    res = []
    for r in range(values.os2(n,k)):
        res.append(combinatorial.unrank_ordered_partition(n, k, r))
    return res


def main():
    print("Random partiton of [|100|] in 50 blocks: ", random_partition(100,50) )
    print("All ordered stirling partitions of [|5|] in 3 blocks in lexicographic order: " )
    for part in exhaust_gen_lex(5,3):
        print("\t",part)
    print("23022000th ordered stirling partition of [|11|] in 6 blocks in lexicographic order:",lexicographic.unrankDicho(11, 6, 23021999) )
    print("===============================")
    print("All ordered stirling partitions of [|5|] in 3 blocks in combinatorial order: " )
    for part in exhaust_gen_combinatorial(5,3):
        print("\t",part)
    print("23022000th ordered stirling partition of [|11|] in 6 blocks in combinatorial order:", combinatorial.unrank_ordered_partition(11, 6, 23021999) )


if __name__ == "__main__":
    main()
