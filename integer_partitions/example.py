
import random

from pathlib import Path
import sys 
THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import combinatorial
import lexicographic
import integer_partitions.values as values
import lex_order

def random_partition(n,k):
    r = random.randint(0,values.count_integer_part(n,k)-1)
    return lexicographic.lex_unrank_part_pref(n,k,r)
def exhaust_gen(n,k):
    res = []
    for r in range(values.count_integer_part(n,k)-1):
       res.append( lexicographic.lex_unrank_part_pref(n,k,r))
    return res
def unranking(n,k,r):
    return lexicographic.lex_unrank_part_pref(n,k,r)

def exhaust_gen_comb(n,k):
    res = []
    for r in range(values.count_integer_part(n,k)-1):
       res.append( combinatorial.unrank_integer_part(n,k,r))
    return res
def unranking_comb(n,k,r):
    return combinatorial.unrank_integer_part(n,k,r)
def main():
    print("Random partition of 100 into 10 parts:", random_partition(100,10))
    print("All partitions of 10 into 3 parts in lex order:")
    print("\t", exhaust_gen(10,3))
    print("3rd partition of 10 into 3 parts in lexicographic order:", unranking(10,3,2))
    print("==========")
    print("All partitions of 10 into 3 parts in combinatorial order:")
    print("\t", exhaust_gen_comb(10,3))
    print("3rd partition of 10 into 3 parts in combinatorial order:", unranking_comb(10,3,2))

if __name__ == "__main__":
    main()


