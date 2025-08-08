#Functions
"""A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.

There are two types of functions :

Pre-defined functions
User defined functions"""


# First function example: Add 1 to a and store as b
"""a = int (input("Enter any number= "))
def add(a):
    b = 1+a
    print(f"You enter number {a}. And if you add 1 it would {b}")
    return b
add(a)
add (3)
add (4)"""

# Define a function for multiple two numbers
"""
def Mult(a, b):
    c = a * b
    print(c)
    return(c)
    
Mult(12,2)
# Use mult() multiply two floats
Mult(3.4,10.999)
# Use mult() multiply two different type values together
Mult(3,"T.dewan")"""

#Variables
#The input to a function is called a formal parameter.There are 2 types of functions 1.Local 2.Global
#A variable that is declared inside a function is called a local variable. The parameter only exists within the function (i.e. the point where the function starts and stops).
#A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program.

#Example for local variable
"""def square(a):
    b = 1+a #b is local variable
    c = a*a+b
    print (a, "if you square + 1", c)
    return c
square(4)

#Example for Global variable  
X = 3 # Initializes Global variable
Y = square(X)
print(Y)"""

#If there is no return statement, the function returns None. The following two functions are equivalent:
"""def mj ():
    print("Body guard")
mj()
print(mj())

def mj1 ():
    print("Body guard")
    return(None)
mj1()
print(mj1())"""
#(Both functions do the same thing in output, even though one uses an implicit None return and the other an explicit return(None).)

#Adding 2 strings
"""def con(a,b):
    c = a+b
    print(c)
    return(c)
con ("This ","is")
"""

#Functions Make Things Simple
#Block-1
"""a1 = 4
b1 = 5
c1 = a1 + b1 *a1 *b1 - 1
if (c1<0):
    c1 = 0
else:
    c1 = 5

print(c1)

#Block -2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if (c2 < 0):
    c2 = 0
else:
    c2 = 5
print (c2)"""

# Make a Function for the calculation above
def equation (a,b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
    print(c) 

equation(5,4) #a1 = 5 , b1 = 4
equation(0,0) #a2 = 0 , b2 = 0     


 