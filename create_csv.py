from random import randint

with open('doc.csv', 'w+') as f:
    for i in range(1,11):
        p = [ f'Player {i}' ]
        p += [ str(randint(55,99)) for _ in range(15) ]
        s = ','.join(p)
        f.write(s)
        f.write('\n')

