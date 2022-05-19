set1 = {'kiwi', 'banana', 'apple'}
set1.add('orange')

print(set1)

set2 = {'apple', 'kiwi', 'orange'}
my_fruit = {'lemon', 'banana'}

print(set2)
print(my_fruit)

set2.update(my_fruit)

print(set2)
print(my_fruit)

set2.update('tomato')
print(set2)

my_set = {'tomato', 'cucumber', 'peper'}
my_list = ['onion', 'garlic']

my_set.update(my_list)
#my_list.update(my_set) error into the console
print(my_set)
#print(my_list)
