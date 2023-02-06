#
#
#

def and_operator(p,q):
    ''' Receive two logical values and return a list with the ^ operator table '''
    return [ p[i] and q[i] for i in range(len(p))]

def or_operator(p,q):
    ''' Receive two logical values and return a list with the v operator table '''
    return [ p[i] or q[i] for i in range(len(p))]

# shitty code
def conditional(p,q):
    ''' Receive two logical values and return a list with the -> operator table '''
    table = []
    for i in range(len(p)):
        if p[i] and not q[i]:
            table.append(False)
            continue
        table.append(True)
    return table

def exclusive_disjunction(p,q):
    ''' Receive two logical values and return a list with the v_ operator table '''
    table = []
    for i in range(len(p)):
        if p[i] is q[i]:
            table.append(False)
            continue 
        table.append(True)
    return table 

def biconditional(p,q):
    ''' Receive two logical values and return a list with the <-> operator table '''
    return [ p[i] is q[i] for i in range(len(p))]

if __name__ == "__main__":
    p = [ True, True, False, False ]
    q = [ True, False, True, False ]

    print(and_operator(p,q))
    print(or_operator(p,q))
    print(exclusive_disjunction(p,q))
    print(conditional(p,q))
    print(biconditional(p,q))