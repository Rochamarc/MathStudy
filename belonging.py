from numerical_sets import NumericalSet

# Numerical
A = NumericalSet(1,2,3,4,5,6)

# Letters
B = NumericalSet('b', 'a', 'c')
C = NumericalSet('d', 'c', 'f')

b = NumericalSet('b')


# testing
print(B.is_contained(b)) # False
print(B.is_not_contained(b)) # True

print(B.is_contained(B))

print(B.belongs_to('b')) # True
print(B.belongs_to('b')) # False