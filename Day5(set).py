#SETs
"""A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}.
Python will automatically remove duplicate items:
"""
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)#automatically remove duplicate items "rock"

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19","Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)
#2nd way(easy)
name_set = set( ["samira","tanzila","dewan","sinan"])
print(name_set)

#Set Operations
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# Add element to set
A.add("NoNe")
print(A)

# Try to add duplicate element to the set
A.add("NoNe")
print(A)

# Remove the element from set
A.remove("NoNe")
print(A)

# Verify if the element is in the set
print("Back in Black" in A)
print("None" in A)

#Sets Logic Operations
#Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1, album_set2)

#represent these common elements with the intersection of two values.
intersection = album_set1 & album_set2
print(intersection)
# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2))

#You can find all the elements that are only contained in album_set1 using the difference method:
# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))

#The elements in album_set2 but not in album_set1 is given by:
print(album_set2.difference(album_set1))

# Find the union of two sets
print(album_set1.union(album_set2))

# Check if superset
print(set(album_set1).issuperset(album_set2))
# Check if subset
print(set(album_set2).issubset(album_set1))
# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1)) 
# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

#Quiz on Sets
#1.Convert the list ['rap','house','electronic music', 'rap'] to a set:
list_set = set (['rap','house','electronic music', 'rap'])
print(list_set)

#2.Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
print("The sum of A is= ",sum(A))
B = set([1, 2, 2, 1])
print("The sum of B is= ",sum(B))

#3.Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

#4.Find out if album_set1 is a subset of album_set3:
print(album_set1.issubset(album_set3))