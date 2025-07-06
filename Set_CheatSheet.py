#Creating an Empty Set 
empty_set = set() 
fruits = {"apple", "banana", "orange"}
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
#remove
print(fruits.remove("banana"))#Use the `remove()` method to remove a specific element from the set. Raises a `KeyError` if the element is not found.


#subset
print(fruits.issubset(colors))
#Superset
print(set(colors).issuperset(fruits)) # Convert colors to a set before using issuperset
