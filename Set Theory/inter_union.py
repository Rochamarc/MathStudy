from numerical_sets import NumericalSet
from random import randint


A = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
B = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
C = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])

print(A == B == C)

print(A.unity(A.inter(B)) == A)
print(A.inter(A.unity(B)) == A)
print(A.unity(B.inter(C)) == A.unity(B).inter(A.unity(C)))
print(A.inter(B.unity(C)) == A.inter(B).unity(A.inter(C)))