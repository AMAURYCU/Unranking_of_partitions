import  lexicographic, values

def random_partition(n,k):
    import random
    rank = random.randint(0, values.ord_lah_inf_k(n,k)-1)
    return lexicographic.unrank_ordered_lah_lex1(n, k, rank)
def exhaust_gen_lex(n,k):
    res = []
    for r in range(values.ord_lah_inf_k(n,k)):
        res.append(lexicographic.unrank_ordered_lah_lex1(n, k, r))
    return res




def main():
    print("Random ordered lah partition of [|100|] in 50 parts :",random_partition(100,50) )
    print("All ordered lah partitions of [|4|] in 2 parts in lexicographic order :" )
    for part in exhaust_gen_lex(4,2):
        print("\t",part)
    print("23022000th ordered lah partition of [|9|] in 5 parts in lexicographic order:",lexicographic.unrank_ordered_lah_lex1(9, 5, 23021999) )
    print("=====================================")
    print("Combinatorial order not implemented yet" )
  

if __name__ == "__main__":
    main()