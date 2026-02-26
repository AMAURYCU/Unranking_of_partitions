from values import ord_lah_inf_k

def extract(block,dispo):
    ret = []
    for i in block: 
        ##print("i", i, "dispo", dispo, "block", block)
        ret.append(dispo[i-1])
        dispo.remove(dispo[i-1])
    return ret,dispo

def extract_part(part,dispo):
    ##print("part", part)
    ret = []
    for i in part: 
        block,dispo = extract(i,dispo)
        ret.append(block)
    return ret


def unrank_ordered_lah_lex_block1(n,k,r):
    ret = []
    elt = n 
    if elt == 0:
        return ret, r
    while True:
        if r < ord_lah_inf_k(elt,k-1) or elt == 0:
            return ret, r 
        r -= ord_lah_inf_k(elt,k-1)
        add, r = divmod(r, ord_lah_inf_k(elt-1,k))
        ret.append(add+1)
        elt -= 1       


def unrank_ordered_lah_lex1(n,k,r):
    part = []
    size = n 
    nb_block = k
    while nb_block > 0:
        block, r = unrank_ordered_lah_lex_block1(size,nb_block,r)
       # print(block, r)
        part.append(block)
        size -= len(block)
        nb_block -= 1
    return extract_part(part, [i+1 for i in range(n)])
