# MAP
#map(function_to_apply, list_of_inputs)
import sys
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
    
#print squared



items = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, items)

#print squared

#sys.exit()



def add(x):
    return (x+x)
    
print map(add,items)

## Filter

print filter(lambda x: x>3, items)


# Reduce

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
    
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


print product

### dir() list() dict() help() str() int()







