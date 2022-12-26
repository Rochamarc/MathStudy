p = True
q = False


def conditional(p,q):
    if p and not q:
        return False
    return True

def exclusive_disjunction(p,q):
    if p is q:
        return False 
    return True


# Conjução

print("p\tq\t\tp ^ q")
print(f"{p}\t{p}\t\t{p and p}")
print(f"{p}\t{q}\t\t{p and q}")
print(f"{q}\t{p}\t\t{q and p}")
print(f"{q}\t{q}\t\t{q and q}")

print("\n\n")

# Disjunção Lógica

print("p\tq\t\tp v q")
print(f"{p}\t{p}\t\t{p or p}")
print(f"{p}\t{q}\t\t{p or q}")
print(f"{q}\t{p}\t\t{q or p}")
print(f"{q}\t{q}\t\t{q or q}")

print("\n\n")

# Disjunção Exclusiva

print("p\tq\t\tp v_ q")
print(f"{p}\t{p}\t\t{exclusive_disjunction(p,p)}")
print(f"{p}\t{q}\t\t{exclusive_disjunction(p,q)}")
print(f"{q}\t{p}\t\t{exclusive_disjunction(q,p)}")
print(f"{q}\t{q}\t\t{exclusive_disjunction(q,q)}")


print("\n\n")

# Condicional

print("p\tq\t\tp -> q")
print(f"{p}\t{p}\t\t{conditional(p, p)}")
print(f"{p}\t{q}\t\t{conditional(p, q)}")
print(f"{q}\t{p}\t\t{conditional(q, p)}")
print(f"{q}\t{q}\t\t{conditional(q, q)}")


print("\n\n")

# Bicondicional

print("p\tq\t\tp <-> q")
print(f"{p}\t{p}\t\t{p is p}")
print(f"{p}\t{q}\t\t{p is q}")
print(f"{q}\t{p}\t\t{q is p}")
print(f"{q}\t{q}\t\t{q is q}")
