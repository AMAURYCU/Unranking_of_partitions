import random, combinatorial, lexicographic, values



def random_partition(n,k):
    return lexicographic.unrank_lex(n,k,random.randint(0,values.count_lah_part_inf_k(n,k)-1))

def exhaust_part_lex(n,k):
    res = []
    for r in range(values.count_lah_part_inf_k(n,k)):
        res.append(lexicographic.unrank_lex(n,k,r))
    return res

def exhaust_part_combi(n,k):
    res = []
    for r in range(values.count_lah_part_inf_k(n,k)):
        res.append(combinatorial.unrank_lah_inf_k_comb(n,k,r))
    return res


def main():
    print("random partition of [|10|] with at most 3 blocks : ", random_partition(10,3))
    print("All partitions of [|5|] with at most 3 blocks in lex order : ")
    for p in exhaust_part_lex(5,3):
        print("\t",p)
    print("23022000th partition of [|12|] with at most 3 blocks in combinatorial order: ", lexicographic.unrank_lex(12,3,23021999))
    print("=====================================")
    print("All partitions of [|5|] with at most 3 blocks in combinatorial order order : ")
    for p in exhaust_part_combi(5,3):
        print("\t",p)
    print("23022000th partition of [|12|] with at most 3 blocks in combinatorial order: ", combinatorial.unrank_lah_inf_k_comb(12,3,23021999))

if __name__ == "__main__":
    main()