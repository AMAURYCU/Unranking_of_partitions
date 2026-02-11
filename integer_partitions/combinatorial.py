


from pathlib import Path
import sys

THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from values import count_integer_part






def unrank_integer_part(n,k,r):
    if k == 0: 
        return []
    if n == 1: 
        return [1]
    else: 
        if r < count_integer_part(n-1,k-1):
            return [1]+unrank_integer_part(n-1,k-1,r)
        else :
            
            part = unrank_integer_part(n-k,k,r-count_integer_part(n-1,k-1))
            return [r+1 for r in part]
  