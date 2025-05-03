"""In Python, there are different data types: String, Integer, and Float.
These data types can all be contained in a tuple as follows:
string='Disco'
int = 10
float= 1.2 """

#Tuples:
tuple1=("disco",10,1.2)
print(tuple1)
print(type(tuple1))

#Index in tuple
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#Negative Index in tuple
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

# Print the type of value on each index
print(type(tuple1[1]))
print(type(tuple1[0]))
print(type(tuple1[2]))

# Concatenate two tuples
tuple2=tuple1+("Hard Rock", 23, 5.6)
print(tuple2)

# Slice from index 0 to index 2
print(tuple2[0:3])
# Slice from index 3 to index 4
print(tuple2[3:4])

# Get the length of tuple
print(len(tuple2))

#Sorting
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted= sorted(Ratings)
print(RatingsSorted)

#Nested Tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ",NestedT[1])
print("Element 2 of Tuple: ",NestedT[2])
print("Element 3 of Tuple: ",NestedT[3])
print("Element 4 of Tuple: ",NestedT[4])

# Print element on each index, including nest indexes
print("Element 2,0 of Tuple: ",NestedT[2][0])
print("Element 2,1 of Tuple: ",NestedT[2][1])
print("Element 3,0 of Tuple: ",NestedT[3][0])
print("Element 3,1 of Tuple: ",NestedT[3][1])
print("Element 4,0 of Tuple: ",NestedT[4][0])
print("Element 4,1 of Tuple: ",NestedT[4][1])
print("Element 4,1,0 of Tuple: ",NestedT[4][1][0])
print("Element 4,1,1 of Tuple: ",NestedT[4][1][1])

# Print the first element in the second nested tuples
print(NestedT[2][1][0])
print(NestedT[4][0][1])

#Quiz on Tuples
# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock","R&B", "progressive rock", "disco") 
print(genres_tuple)
print(len(genres_tuple))

#1,Access the element, with respect to index 3:
print(genres_tuple[3])
#2,Use slicing to obtain indexes 3, 4 and 5:
print(genres_tuple[3:6])
#3,Find the first two elements of the tuple genres_tuple:
print(genres_tuple[:2])
#4,Find the index of 's' in "disco":
print('disco'.find('s'))
#5,Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
C_tuple=(-5, 1, -3)
print(sorted(C_tuple))
