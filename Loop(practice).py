#Loops are use to repeat instructions. There are 2 types of loops in python- 
#1.While Loop
#2.For loop

#Print & count the word "Hello"
i=1
while i<=5:
    print("Hello")
    print(i)
    i+=1

#Print number 1 to 10
i=1
while i<=10:
    print(i)
    i+=1

#print  number from 10 to 1
i=10
while i>=1:
    print(i)
    i-=1


#Take user input for table and print it from 1 to 10
n = int (input("Enter number for table: "))
i = 1
while i<=10:
    print(i*n)
    i+=1

#Print table in table formate like 5*1=5
n = int (input("enter number: ")) 
i =1
while i<=10:
    print(f"{n}*{i} = {n*i}")
    i+=1

#print the element of following list by using loop[1,4,9,16,25,36,49,64,81,100]
num =[1,4,9,16,25,36,49,64,81,100]
idx =0
while idx<len(num):
    print(num[idx])
    idx+=1

#print ["apple", 'berry', 'mango',"orange","pineapple"]
fruits = ["apple", 'berry', 'mango',"orange","pineapple"]
idx = 0
while idx<len(fruits):
    print(fruits[idx])
    idx+=1