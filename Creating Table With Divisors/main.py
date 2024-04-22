from random import choice 

from tabulate import tabulate

from lib import get_divisions, fill_line

values = get_divisions()
# print(values)

# To store all the results
results = []

for _ in range(20):
    data = []

    for _ in range(4):
        # Here we create a 4x4 matrix 

        line = fill_line(values, 4)
        
        # for _ in range(4):
        #     list_pointer = choice(values) # get the operation

        #     # Store the operation in line and the answer to the results 
        #     line.append(list_pointer[0])
        #     results.append(list_pointer[-1])
        
        data.append(line)

    print(tabulate(data, tablefmt="simple_grid"))
    # print(results)

# Remove duplicates    
results = set(results)
print(results)
