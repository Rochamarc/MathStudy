val = int(input("Type a number: "))

ns = [ (2*n-1) for n in range(1,val+1) ]

for i in range(1,val+1):
    print(f"{sum(ns[:i])} == {i}**2 ", sum(ns[:i])==i**2)
