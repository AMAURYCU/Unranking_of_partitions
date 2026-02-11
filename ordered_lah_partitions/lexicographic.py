

from values import count_ordered_lah_rec as ordered_lah_rec


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

def unrank_ordered_lah_lex_block(n,k,r):
    ret = []
    elt = n 
    nb = ordered_lah_rec(n,k) // elt 
    add, r= divmod(r, nb)
    ret.append(add+1)
    elt -= 1 
    while True:
        if r < ordered_lah_rec(elt,k-1):
            return ret, r 
        r -= ordered_lah_rec(elt,k-1)
        #print("r =", r)
        nb = ordered_lah_rec(elt,k) // elt
        add, r = divmod(r, nb)
        ret.append(add+1)
        elt -= 1 
        n -= 1 

        
def unrank_ordered_lah_lex(n,k,r):
    part = []
    size = n 
    nb_block = k
    while nb_block > 0:
        block, r = unrank_ordered_lah_lex_block(size,nb_block,r)
        ##print(block)
        part.append(block)
        size -= len(block)
        nb_block -= 1
    return extract_part(part, [i+1 for i in range(n)])
