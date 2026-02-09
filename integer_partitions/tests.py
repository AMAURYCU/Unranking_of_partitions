"""Smoke tests for integer_partitions."""

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

def run():
    print("Smoke test for integer_partitions")
    try:
        print("combinatorial:", combinatorial.combinatorial_info())
    except Exception as e:
        print("combinatorial import error:", e)
    try:
        print("lexicographic:", lexicographic.lexicographic_info())
    except Exception as e:
        print("lexicographic import error:", e)



# prop : r1 < r2 => leq_lex_seq(unrank_integer_part(n,k,r1), unrank_integer_part(n,k,r2) and not eq_seq(unrank_integer_part(n,k,r1), unrank_integer_part(n,k,r2))
def correction(n,k):
    old = [n*k]
    for r in range(values.count_integer_part(n,k)-1,-1 , -1):
       part = lexicographic.lex_unrank_part_pref(n,k,r)
       if not (lex_order.leq_lex_seq(part, old)and  not lex_order.eq_seq(part, old)):
            print("Error at n =", n, "k =", k, "r =", r)
            print("part =", part, "old =", old)
            return False
       old = part
    return True


    




if __name__ == "__main__":
    print(correction(100, 10))
