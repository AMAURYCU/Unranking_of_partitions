from  values import count_lah_part_inf_k as lahinf_k 



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
    s_up = lahinf_k(n-(size-1),k)- (n-size)*lahinf_k(n-size,k)
    while True :
        if not contains1:

            if r< s_up:
                bigL = lahinf_k(n-size,k-1)
                block.append(1)
                if r < bigL:
    
                    return block, r 
                else:
                    r -= bigL
                    size += 1
                    contains1 = True 
                s_up = lahinf_k(n-(size-1),k)- (n-size)*lahinf_k(n-size,k)
            else:
                r -= s_up
                sdown = lahinf_k(n-size, k )
                elt, r = divmod(r,sdown)
                block.append(elt+2)
                size += 1
                s_up = lahinf_k(n-(size-1),k)- (n-size)*lahinf_k(n-size,k)   
        else: 

            elt,r = divmod(r,s_up)
            block.append(elt+1)
            bigL = lahinf_k(n-size,k-1)
            if r < bigL:
                return block, r
            r = r - bigL
            size += 1
            s_up = lahinf_k(n-(size-1),k)- (n-size)*lahinf_k(n-size,k)
          
def unrank_lex(n, k,r):
    n0 = n
    Res = []
    while n > 0:
        A, r = block_lex_unrank(n, k,r)
        Res.append(A)
        n -= len(A)
        k-= 1
    Res = extract_part(Res, list(range(1, n0+1)))
    return Res


