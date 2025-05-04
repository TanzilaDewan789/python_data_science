fruits = ['Apple','Banana','Mango',]
#List.append('Take one argument')
fruits.append('Orange')
print(fruits)

#List.extend('iterable, take more than one argument')
more_fruits = ['Blueberry','cherry']
fruits.extend(more_fruits)
print(fruits)
fruits.extend('Grape')#separate the word character by character
print(fruits)

#Copy
my_list=[1,2,3,2,4,2,5,2,2]
print(my_list)
new_list=my_list.copy()
print(new_list)

#Count --> count the frequent of an element 
count = my_list.count (2)
print(count)

#delete index
del my_list[2]
print(my_list)

#pop() remove the element and return the last element
removed =my_list.pop()
print(removed)
print(my_list)#return without last element

#remove(element)--> remove the specific element
my_list.remove(2)# if there is copy of any element it will remove the 1st one
print(my_list)


#Indexing ->start from 0,1,2... negative -1,-2,-3
names = ['Tanzila','bin', "abdus",'Samad']
print(names[0])


#insert() 
numbers = [1,2,5,5,5,6,7,8]
#does not take more than 2 argument
#numbers.insert(1,2,3,4,5)
#print(names)---> error
numbers.insert(4,10)#4 is index & 10 number that insert in the 4th index
print(numbers)

numbers.insert(3,'samira')
print(numbers)

#Modifying a list
numbers[2]= 'tanzila'#modified in index 2
print(numbers)

#reverse()--> reverse the list
numbers_id = [9,8,7,6,5,4,3,2,1,0]
numbers_id.reverse()
print(numbers_id)

#Slicing--> You can use slicing to access a range of elements from a list.
#syntax-->list_name[start:end:step] 
Heart_Rate=[77,65,66,60,90,95,60]
print(Heart_Rate[2:5])
print(Heart_Rate[:6])
print(Heart_Rate[3:])
print(Heart_Rate[::2])#every 2nd 
print(Heart_Rate[::3])#every #3rd 


#sort()
#Increasing Order
Heart_Rate.sort()
print(Heart_Rate)
#Decreasing Order
Heart_Rate.sort(reverse=True)
print(Heart_Rate)