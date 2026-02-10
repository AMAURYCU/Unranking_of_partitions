# Auto-generated placeholder
"""lexicographic module (placeholder)

Utilities for lexicographic ordering helpers for unranking algorithms.
"""

from  values import count_lah_part as lah

def extract(block,dispo):
    ret = []
    for i in block: 
        ret.append(dispo[i-1])
        dispo.remove(dispo[i-1])
    return ret,dispo

def extract_part(part,dispo):
    ret = []
    for i in part: 
        block,dispo = extract(i,dispo)
        ret.append(block)
    return ret



def block_lex_unrank(n,k,r):
    block = []
    size = 1
    contains1 = False 
    s_up = lah(n-(size-1),k)- (n-size)*lah(n-size,k)
    while True :
        if not contains1:
            if r< s_up:
                bigL = lah(n-size,k-1)
                block.append(1)
                if r < bigL:
                    return block, r 
                else:
                    r -= bigL
                    size += 1
                    contains1 = True 
                s_up = lah(n-(size-1),k)- (n-size)*lah(n-size,k)
            else:
                r -= s_up
                sdown = lah(n-size, k )
                elt, r = divmod(r,sdown)
                block.append(elt+2)
                size += 1
                s_up = lah(n-(size-1),k)- (n-size)*lah(n-size,k)   
        else: 
            elt,r = divmod(r,s_up)
            block.append(elt+1)
            bigL = lah(n-size,k-1)
            if r < bigL:
                return block, r
            r = r - bigL
            size += 1
            s_up = lah(n-(size-1),k)- (n-size)*lah(n-size,k)
          
def unrank_lah_lex(n,k,r):
    part = []
    size = n 
    nb_block = k
    for l in range(k):
        block, r = block_lex_unrank(size,nb_block,r)
        part.append(block)
        size -= len(block)
        nb_block -= 1
    return extract_part(part,list(range(1,n+1)))