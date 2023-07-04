# Logical Operators


def denial(p):
    ''' Receive p and return not p '''
    return not p

def conjuction(p,q):
    ''' Receive p and p and return p and q '''
    return p and q

def disjuction(p,q):
    ''' Receive p and q and return p or q '''
    return p or q

def exclusive_disjunction(p, q):
    ''' Receive p and q and return or p or q '''
    return p is not q

def conditional(p,q):
    ''' Receive p and q and return p -> q '''
    return False if p and not q else True


def biconditional(p,q):
    ''' Receive p and q and return p <-> q '''
    return p is q
