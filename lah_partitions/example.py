

import combinatorial, lexicographic, values, random
def exhaust_gen_lex(n,k):
    res = []
    for r in range(values.count_lah_part(n,k)):
        res.append(lexicographic.unrank_lah_lex(n,k,r))
    return res
def exhaust_gen_comb(n,k):
    res = []
    for r in range(values.count_lah_part(n,k)):
        res.append(combinatorial.unrank_lah_partition(n,k,r))
    return res
def main():
    print("Random partition of [|100|] in 10 blocks", lexicographic.unrank_lah_lex(100,10,random.randint(0, values.count_lah_part(100,10)-1)))
    print("All partitions of [|5|] in 4 blocks in lex order:" )
    for p in exhaust_gen_lex(5,4):
        print("\t", p)
    print("23022000^th partition of [|15|] in 8 blocks in lex order:", lexicographic.unrank_lah_lex(15,8,23021999))
    print("==================================")
    print("All partitions of [|5|] in 4 blocks in combinatorial order:")
    for p in exhaust_gen_comb(5,4):
        print("\t", p)
    print("23022000^th partition of [|15|] in 8 blocks in combinatorial order:", combinatorial.unrank_lah_partition(15,8,23021999))

if __name__ == "__main__":
    main()
