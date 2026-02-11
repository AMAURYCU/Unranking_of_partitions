


from pathlib import Path
import sys

THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from values import count_integer_part
import sys 
sys.setrecursionlimit(10**9)


v = 0
def lex_unrank_part_pref(n,k,r):
    acc = []
    lem = 2
    if k == n: 
        return [1] * k
    if k == 1:
        return [n]
    if r < count_integer_part(n-1,k-1):
        acc = [1]
        lem = 1 
        n -= 1 
        k-= 1
    else:
        r = r -  count_integer_part(n-1,k-1)
    for _ in range(1,k+1):
        if k == 1:
                acc.append(n)
                return acc 
        for j in range(lem, n-k+1):
            global v
            v += 1
            magic = count_integer_part(n-j-(k-1)*(j-1),k-1)
            if r < magic:
                acc.append(j)
                n -= j 
                k -= 1 
                lem = j 
                break 
            r -= magic
    return acc 



