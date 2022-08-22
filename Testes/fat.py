def product(*values):
    a = 1
    for i in values:
        a *= i
    return a 

def factorial(value):
    return product(*[ i for i in range(value, 1,-1) ])
    
for i in range(1, 21):
    print(f"{i}! == {factorial(i)}")