#Before we discuss loops lets discuss the range object. It is helpful to think of the range object as an ordered list.
print(range(3))
#range through loop
for i in range(0,8):
    print(i)

#LOOP-
"""There are 2 types of loops in Python-
1.For Loop
2.While Loop"""

#FOR LOOP
#The for loop enables you to execute a code block multiple times. 
#1.Simple syntax 
fruits =["Apple", "Mango", "Apricot"]
for x in fruits:
    print(x)



#Let's try to use a for loop to print all the years presented in the list dates:
#1.1
dates = [1999,2000,2001]
N = len(dates)

for i in range (N):
    print(dates[i])

#1.2
for year in dates:
    print(year)

#2.1
"""squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])"""

#2.2(Loop through the list and iterate on both index and element value)
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)