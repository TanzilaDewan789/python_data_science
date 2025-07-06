empty_set = set() #Creating an Empty Set 
fruits = {"apple", "banana", "orange"}
colors = ("orange", "red", "green")
empty_set.update(fruits)
empty_set.update(colors)
print(empty_set)
empty_set.discard("apple")
print(empty_set)