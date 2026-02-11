"""Exemple d'utilisation pour ordered_lah_partitions."""

import combinatorial, lexicographic, values

def random_partition(n,k):
    import random
    rank = random.randint(0, values.count_ordered_lah_rec(n,k)-1)
    return lexicographic.unrank_ordered_lah_lex(n, k, rank)
def exhaust_gen_lex(n,k):
    res = []
    for r in range(values.count_ordered_lah_rec(n,k)):
        res.append(lexicographic.unrank_ordered_lah_lex(n, k, r))
    return res

def exhaust_gen_combinatorial(n,k):
    res = []
    for r in range(values.count_ordered_lah_rec(n,k)):
        res.append(combinatorial.unrank_ordered_lah_partition(n, k, r))
    return res


def main():
    print("Random ordered lah partition of [|100|] in 50 parts :",random_partition(100,50) )
    print("All ordered lah partitions of [|4|] in 2 parts in lexicographic order :" )
    for part in exhaust_gen_lex(4,2):
        print("\t",part)
    print("23022000th ordered lah partition of [|9|] in 5 parts in lexicographic order:",lexicographic.unrank_ordered_lah_lex(9, 5, 23021999) )
    print("lexicographic:", lexicographic.lexicographic_info())
    print("=====================================")
    print("All ordered lah partitions of [|4|] in 2 parts in combinatorial order :" )
    for part in exhaust_gen_combinatorial(4,2):
        print("\t",part)
    print("23022000th ordered lah partition of [|9|] in 5 parts in combinatorial order:", combinatorial.unrank_ordered_lah_partition(9, 5, 23021999) )


if __name__ == "__main__":
    main()
