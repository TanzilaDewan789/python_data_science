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
print(album_set1)
print(album_set2)
print(album_set1, album_set2)