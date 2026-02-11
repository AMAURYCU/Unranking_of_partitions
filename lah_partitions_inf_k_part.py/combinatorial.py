import values 


def unrank_lah_partition(n,k,r):
    if k == 0: 
        return []
    if n == 0: 
        return []
    if r < (n-1+k)*values.count_lah_part(n-1,k):
        pos, r = divmod(r, values.count_lah_part(n-1,k))
        part = unrank_lah_partition(n-1,k,r)
        for l in part: 
            pos = pos-len(l)-1
            if pos < 0:
                pos = len(l)+1+pos
                l.insert(pos,n)
                break 
        return part 
    r -= (n-1+k)*values.count_lah_part(n-1,k)
    
    part = unrank_lah_partition(n-1,k-1,r)
    part.append([n])
    return part

def unrank_lah_inf_k_comb(n,k,r):
    for i in range(1,k+1):
        if r < values.count_lah_part(n,i):
            res = unrank_lah_partition(n,i,r)
            return res
        r -= values.count_lah_part(n,i)






