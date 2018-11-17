var = 123
d = [1,2,3,4]
dic = { 'one', 1 }

comb = [1,2, {'w':3, 'r': [1,2,3,] }]

import json

def add(x,y):
    z = x+y
    print ('Rezult = %s' % z)


f = open('1.json', 'w')
f.write(json.dumps(comb))
f.close()

f = open('1.json', 'r')
rez = f.read()
n = 123
c = 43543
import ipdb; ipdb.set_trace()

add(1,2)
add(3,4)
add(5,6)

print rez
