#Loops are use to repeat instructions. There are 2 types of loops in python- 
#1.While Loop
#2.For loop


       #1.WHILE LOOP


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

#traverse(Linear search)
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


#Search for a number x in this tuple using loop(Linear Search)
num = (1,4,9,16,25,36,49,64,82,100,36)
x=36
i = 0
while i<len(num):
    if(num[i]==x):
        print("Found at index: ",i)
    else:
        print("Not found")
    i+=1


#Break: use to terminate the loop when encounter
num = (1,4,9,16,20,25,36,49,64,82,100,36)
x=20
i=0
while i<len(num):
    if num[i]==x :
        print("Found at index : ",i)
        break
    else:
        print('Not found')
    i+=1  


#code doesn't run after break
i=1
while i <= 5:
    print(i)
    if (i==3):
        break
    i+=1
print("Loop end")



#Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration.
i = 1
while i <= 5:
    if(i == 3):
       i += 1
       continue #skip
    print(i)
    i += 1


#print all odd numbers from 1 to 10
i = 1
while i<=10:
    if(i%2 == 0):
        i += 1
        continue
    print("Odd number= ", i)
    i += 1


#print all the even numbers from 1 to 10
i = 1 
while i <= 10 :
    if (i %2 != 0):
        i += 1
        continue
    print ("even number= ", i)
    i += 1


       #2. FOR LOOP
#For loop are used for sequential traversal, for traversing list, string, tuples, etc

#printing a list  in for loop
List = [1,2,3,4,5]
for el in List:
    print (el)

#print vegetables name in list using for loop
vegetables = ["Potato",'Ladyfinger',"Zucchini","Tomato"]
for veg in vegetables:
    print(veg)


#tuples in loop
tup = (1,2,3,4,5,6,7,8,9)
for List_num in tup:
    print(List_num)   



#strings in for loop
name = "Tanzila"
for str in name:
    print(str)
else:
    print("END")#use as break


#finding character "z" in string "Tanzila" using for 
name = "Tanzila"
for  str  in name:
    if (str == "z"):
        print("z found")
        break 
    print(str)
    
else:
    print("END")


              #range (start, stop, step/increment/ decrement)
#range function return a sequence of numbers starting from 0 by default & increment by 1 by default & stop before the specific number.

#print 0 to 5 in range function 
print(range(5))


#range (stop)
for i in range(6):
    print(i)


#range(start, stop)
for i in range (2,5):
    print(i)

#range(start, stop, step)
for i in range (2, 10, 2):
    print(i)

#print all the even number from 0 to 20
for i in range (0,51,2):
    print("Even: ",i)


#print all the odd numbers from 1 to 20
for i in range (1,20,2):
    print ("Odd: ",i)

#print numbers from 1 to 50
for i in range (51):
    print (i)

#print numbers from 50 to 1
for i in range (50,0,-1):
    print("Back tracking : ",i)


#print multiplication table of n
n = int (input("enter any number: "))
for i in range (1, 11):
    print (i*n)


        #Press statement 

#Press is null statement that does nothing, its used as placeholder for future code.
for i in range (5):
    pass
if i >5:
    pass
print("Work for later")

         #QUIZ
#Find the sum of first na Natural numbers 
#For loop
n = 5
sum = 0
for i in range (1, n+1):
    print (i)
    sum += i
print("Total sum is= ", sum)

#While loop
n=5
sum =0 
i=1 
while i<=n:
    print(i) 
    sum += i
    i +=1

print("Sum ",sum)


#find the factorial of first n natural number
#While loop
n = 5
fact = 1
i = 1
while i <=n:
    fact =fact * i
    i += 1 
print ("FActorial = ", fact)

#For loop
n = 6
fact =1 
for i in range (1, n+1):
    fact = fact * i
    print("Factorial: ", fact)