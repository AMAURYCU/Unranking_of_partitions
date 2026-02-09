def leq_lex_seq(a,b):
    try :
        for i in range(len(a)):
            if a[i] < b[i]:
                return True 
            elif a[i] > b[i]:
                return False
        return True

    except Exception as e:
        return False 
    

def leq_lex_part(a,b):
    for i in range(len(a)):
        if not leq_lex_seq(a[i], b[i]):
            return False
    return True



def eq_seq(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def eq_part(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if not eq_seq(a[i], b[i]):
            return False
    return True