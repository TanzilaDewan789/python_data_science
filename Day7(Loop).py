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


#What is while loop?
""" what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value."""
# what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")