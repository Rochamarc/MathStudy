from numerical_sets import NumericalSet

A = NumericalSet(2,4,6,8,10,12) # multiplos de 2
B = NumericalSet(3,6,9,12,15,18) # multiplos de 3
C = NumericalSet(5,10,15,20,25,30) # multiplos de 5
O = NumericalSet() # Conjunto Vazio
U = NumericalSet(1) # Valor unitario 
 
# Unity properties
#
# A U A = A
# A U {} = A
# A U B = B U A
# (A U B) U C = A U (B U C)
#

AUA = A.unity(A)
AUO = A.unity(O)
AUB = A.unity(B)
BUA = B.unity(A)
BUC = B.unity(C)
AUB_UC = AUB.unity(C)
AU_BUC = A.unity(BUC)

# Validating
print("A U A = A ", AUA==A) # True
print("A U {} = A ", AUO==A) # True
print("A U B = B U A", AUB==BUA) # True
print("(A U B) U C = A U (B U C) ", AUB_UC==AU_BUC) # True


print("\n\n\n==========================================\n\n\n")


# 
# Inter properties
# 
# A I A = A
# A I {} = A
# A I B = B I A
# A I (B I C) = (A I B) I C
#


AIA = A.inter(A)
AIU = A.inter(U)
AIB = A.inter(B)
BIA = B.inter(A)
BIC = B.inter(C)
AI_BIC = A.inter(BIC)
AIB_IC = AIB.inter(C)

# Validating
print("A I A = A ", AIA==A) # True
print("A I {} = A ", AIU==A) # True
print("A I B = B I A ", AIB==BIA) # True
print("A I (B I C) = (A I B) I C", AI_BIC==AIB_IC) # True
