#Creating an Empty Set 
empty_set = set() 
fruits = {"apple", "banana", "orange",'cherry'}
colors = ("orange", "red", "green")

#putting all those sets in empty_set
empty_set.update(fruits)
empty_set.update(colors)
print(empty_set)

#discard
empty_set.discard("apple")#Use the `discard()` method to remove a specific element from the set. Ignores if the element is not found.
print(empty_set)

#pop
print(fruits.pop())# It raises a `KeyError` if the set is empty. Use this method to remove elements when the order doesn't matter.

#remove-1(output:None)
"""print(fruits.remove("banana"))"""#Use the `remove()` method to remove a specific element from the set.Does not anything.

#remove-2(Just removes the specified element from a set)
"""fruits.remove("cherry")
print(fruits)"""

#subset
print(fruits.issubset(colors))
#Superset
print(set(colors).issuperset(fruits)) # Convert colors to a set before using issuperset

#union/combined
print(fruits.union(colors))

#intersection/common
print(fruits.intersection(colors))

#difference
print(fruits.difference(colors))


#clear
print(fruits.clear())

#copy
new_fruits = fruits.copy()
print(new_fruits)
#Update
new_fruits.update(['Kiwi','grape'])
print(new_fruits)
#Add
new_fruits.add('mango')
print(new_fruits)