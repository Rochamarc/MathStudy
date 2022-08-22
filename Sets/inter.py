from numerical_sets import NumericalSet
from random import randint


A = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
B = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
C = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
U = NumericalSet()

print(A == B == C == U) # Prove that they are 3 sets any and different

print(A.inter(A) == A)
print(A.inter(U) == A) # It should return True 
print(A.inter(B) == B.inter(A))
print(A.inter(B.inter(C)) == A.inter(B).inter(C))
