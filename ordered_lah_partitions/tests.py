from pathlib import Path
import sys

THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
import lex_order

import values
import lexicographic



def well_formed(n,p):
    """
    check that p is a well formed ordered lah partition of [|n|]: 
    - fa x in [|n|], x is in exactly one block of p 
    - each block of p contains at least 1 element
    """ 
    d = [False for i in range(n+1)]
    for block in p: 
        if block == []:
            return False 
        for elt in block: 
            if elt < 1 or elt > n:
                return False 
            if d[elt-1]: 
                return False 
            d[elt-1] = True
    return True
                
def correction(n,k, verbose = True):
    p0 = lexicographic.unrank_ordered_lah_lex(n,k,0)
    for r in range(1, values.count_ordered_lah_rec(n,k)):
        if verbose: 
            if r % 1000 == 0:
                print("r =", r,"/", values.count_ordered_lah_rec(n,k))
        p = lexicographic.unrank_ordered_lah_lex(n,k,r)
        if not well_formed(n,p):
            print("Error at n =", n, "k =", k, "r =", r)
            print("part =", p)
            return False
        if (not lex_order.lt_lex_part(p0,p)):
            print("Error at n =", n, "k =", k, "r =", r)
            print("p =", p, "p0 =", p0)
            return False
        p0 = p
    return True
            


if __name__ == "__main__":
    print(correction(8,4))

