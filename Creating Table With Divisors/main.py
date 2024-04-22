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
        
        # Save the results
        results += [ l[-1] for l in line ]

        # remove the results from the line
        line = [ l[0] for l in line ]

        data.append(line)

    print(tabulate(data, tablefmt="simple_grid"))
    # print(results)

# Remove duplicates    
results = set(results)
print(results)
