#Creating on list
List=["Tanzila",1,'time',6.0,7.99,"Rain"] #Positive index starting from 0,1,2..left to right
print(List)
# List slicing
print(List[2:5])


#.extend- use for added new element in the list
List.extend(["Vector","Logarithm"])
print(List)

List.extend("Tom")#will add but separately
print(List)

#.append-use for one element in the list as nested list
List.append(["Tim","Charls"])
print(List)

# Change the element based on the index
List[0]="Samira"
print(List)

# Delete the element based on the index
del(List[7])#Build in method
print(List)

# Split the string, default is by space
A='My name is tanzila'
print(A.split())#Build in  method

# Copy (copy by reference) the list A
a=['apple','mango',80]
print(a)
b=a
print(b)
# Examine the copy by reference
print('b[0]:', b[0])
a[0]="papaya"
print(a)
print('b[0]:',b[0])

#Quiz on List
"""1.Create a list a_list, with the following elements 1, hello, [1,2,3] and True
2.Find the value stored at index 1 of a_list.
3.Retrieve the elements stored at index 1, 2 and 3 of a_list."""

a_list=[1,'hello',[1,2,3],True]
print(a_list)#1
print(a_list[1])#2
print(a_list[1:4])

#4.Concatenate(add) the following lists A = [1, 'a'] and B = [2, 1, 'd']
A = [1, 'a'] 
B = [2, 1, 'd']
print(A+B)
print("Tanzila")