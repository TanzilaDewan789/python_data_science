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

def Mult(a, b):
    c = a * b
    print(c)
    return(c)
    
Mult(12,2)
# Use mult() multiply two floats
Mult(3.4,10.999)
# Use mult() multiply two different type values together
Mult(4,"T.dewan")