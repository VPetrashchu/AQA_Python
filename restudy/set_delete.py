set1 = {'tomato', 'potato', 'cabbage', 'fish', 'milk'}

set1.remove('tomato')
print(set1)

set1.discard('potato')
print(set1)

x = set1.pop()
print(x) # deleted value
print(set1)

set_clear = {'bread', 'sugar', 'salt'}
set_clear.clear()
print(set_clear)

set_delete = {'apple', 'banana', 'cherry'}
del set_delete

print(set_delete) #this will raise an error because the set no longer exists