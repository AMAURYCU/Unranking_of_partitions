import random, combinatorial, lexicographic, values



def random_partition(n,k):
    return lexicographic.unrankDicho(n,k,random.randint(0,values.Bs2(n,k)-1))

def exhaust_part_lex(n,k):
    res = []
    for r in range(values.Bs2(n,k)):
        res.append(lexicographic.unrankDicho(n,k,r))
    return res

def exhaust_part_combi(n,k):
    res = []
    for r in range(values.Bs2(n,k)):
        res.append(combinatorial.unrank_comb(n,k,r))
    return res


def main():
    print("random partition of [|10|] with at most 4 blocks : ", random_partition(10,4))
    print("All partitions of [|5|] with at most 4 blocks in lex order : ")
    for p in exhaust_part_lex(5,4):
        print("\t",p)
    print("230220th partition of [|14|] with at most 4 blocks in combinatorial order: ", lexicographic.unrankDicho(14,4,230219))
    print("=====================================")
    print("All partitions of [|5|] with at most 4 blocks in combinatorial order order : ")
    for p in exhaust_part_combi(5,4):
        print("\t",p)
    print("230220th partition of [|14|] with at most 4 blocks in combinatorial order: ", combinatorial.unrank_comb(14,4,230219))

if __name__ == "__main__":
    main()