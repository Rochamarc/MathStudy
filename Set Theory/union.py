from numerical_sets import NumericalSet
from random import randint


A = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
B = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
C = NumericalSet(*[ randint(0,10) for _ in range(randint(2,20)) ])
O = NumericalSet()

print(A == B == C == O) # Prove that they are 3 sets any and different

# Now we are gonna test their properties
print(A.unity(A) == A) # A U B = A
print(A.unity(O) == A) # A U {} = A
print(A.unity(B) == B.unity(A)) # A U B = B U A
print(A.unity(B).unity(C) == A.unity(B.unity(C))) # (A U B) U C = A U (B U C) 

