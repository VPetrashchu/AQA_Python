#union() method returns a new set with all items from both sets

set1 = {'apple', 'orange', 'kiwi'}
set2 = {'android', 'apple', 'microsoft'}

set_join = set1.union(set2)
print(set_join)
print(' ')

set3 = {1,2,3}
set4 = {'a', 'b', 'c',}


#update() method inserts the items in set2 into set1
set3.update(set4)
print(set3)

#intersection_update() method will keep only the items that are present in both sets.
set1.intersection_update(set2)
print('keep only duplicate - set1', set1)
print('set2', set2)
print(' ')

#return a set that contains the items that exist in both set z, and set p:
z = {'tomato', 'potato', 'peper'}
p = {'peper', 'salt', 'sugar'}

t = z.intersection(p)
print(t)
print(z)
print(p)
print(' ')

#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
n = {'tomato', 'potato', 'peper'}
k = {'peper', 'salt', 'sugar'}
print('set n without changes', n)
print('set k without changes', k)

n.symmetric_difference_update(k)
print('show not same items - set n', n)
print('set k', k)
print(' ')

#symmetric_difference return a set that contains all items from both sets, except items that are present in both
r = {'tomato', 'potato', 'peper'}
u = {'peper', 'salt', 'sugar'}

print('set r without changes', r)
print('set u without changes', u)

finish_result = r.symmetric_difference(u)
print('show only same items - set finish', finish_result)
print('set u', u)
print(' ')
