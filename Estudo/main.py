import pandas as pd

fl = None

with open('cronograma_1.csv', 'r', encoding='utf8') as f:
    fl = f.readlines() 

header = fl[0].split(',')
header[-1] = header[-1].replace('\n','')

print(header)

content = fl[1::]

for i in enumerate(content):
    content[i[0]] = content[i[0]].replace('\n','')
    content[i[0]] = content[i[0]].split(',')

for i in content:
    print(i)

df = pd.DataFrame(content, columns=header)
print(df)
