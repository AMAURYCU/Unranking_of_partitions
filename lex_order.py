def lt_lex_seq(a,b):
    try:
     for i in range(len(a)):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False
     return len(a) <len(b)

    except Exception as e:
        
        return False

def lt_lex_part(a,b):
    for i in range(len(a)):
        if lt_lex_seq(a[i], b[i]):
            return True
        if lt_lex_seq(b[i], a[i]):
            return False
    return False
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


