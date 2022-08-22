from numerical_sets import NumericalSet 
from random import randint, choice

''' B and C subsets of A'''

A = NumericalSet(*[ randint(0,10) for _ in range(randint(5,20)) ])
B = NumericalSet(*[ choice(A.set) for _ in range(randint(2,20)) ])
C = NumericalSet(*[ choice(A.set) for _ in range(randint(2,20)) ])
O = NumericalSet()

print(A == B == C == O)

print(A.additional(B).inter(B) == O and A.additional(B).unity(B) == A) # Two propositions only True if both are true
print(A.additional(A) == O and A.additional(O) == A) # Two propositions
print(A.additional(B.inter(C)) == A.additional(B).unity(A.additional(C)))
print(A.additional(B.unity(C)) == A.additional(B).inter(A.additional(C)))