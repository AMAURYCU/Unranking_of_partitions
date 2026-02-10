"""Smoke tests for lah_partitions."""

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
import values
import lex_order


def well_formed(n, p):
    """
    check that p is a well formed lah partition of [|n|]: 
    - fa x in [|n|], x is in exactly one block of p
    - each block of p contains at least 1 element 
    - p is in canonical form 
    - x in p => x in [|n|]
    """
    d = {i:False for i in range(1,n+1)}
    old_block = [0]
    for block in p: 
        if block == []:
            return False 
        for elt in block: 
            if elt < 1 or elt > n:
                return False 
            if d[elt]: 
                return False 
            d[elt] = True
        if not min(old_block) < min(block):
             return False 
        old_block = block
        

    return True 



def correction(n,k, verbose = True):
    """
   check that the unranking algorithm produces well formed lah partitions and all the lah partitions of [|n|] with k blocks are produced.
    """
    old = lexicographic.unrank_lah_lex(n,k,0)
    for r in range(1,values.count_lah_part(n,k)):
         if verbose: 
              if r % 1000 == 0:
                    print("r =", r,"/", values.count_lah_part(n,k))
         part = lexicographic.unrank_lah_lex(n,k,r)
         if not well_formed(n,part):
                print("Error at n =", n, "k =", k, "r =", r)
                print("part =", part)
                return False
         if not lex_order.leq_lex_seq(old, part) or lex_order.eq_seq(old, part):
                print("Error at n =", n, "k =", k, "r =", r)
                print("part =", part, "old =", old)
                return False
        
         old = part
    return True 

if __name__ == "__main__":
   # print(well_formed(10, [[1,2],[3,4,7,8,9,10], [5,6]]))
    print(correction(9,3))
         
