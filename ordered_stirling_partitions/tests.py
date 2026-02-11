from pathlib import Path
import sys

THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
import lex_order
import lexicographic
import values 


def is_well_formed(p,n):
    """
    Check if all block of p is a strictly increasing sequence of integers each between 1 and n
    Check if the blocks of p are disjoint and their union is [|n|]
    Check if none of the block of p is empty 
    """
    dispo = set(range(1,n+1))
    for block in p:
        if len(block) == 0: 
            return False 
        for elt in block: 
            if elt < 1 or elt > n: 
                return False 
            if elt not in dispo: 
                return False 
            dispo.remove(elt)
    return len(dispo) == 0
def correction(n,k, verbose = True):
    p0 = lexicographic.unrankDicho(n,k,0)
    for r in range(1, values.os2(n,k)):
        if verbose: 
            if r % 1000 == 0:
                print("r =", r,"/", values.os2(n,k))
        p = lexicographic.unrankDicho(n,k,r)
        if not is_well_formed(p,n):
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
    print(correction(9,6))
