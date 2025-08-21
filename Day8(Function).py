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
"""def equation (a,b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
    print(c) 

equation(5,4) #a1 = 5 , b1 = 4
equation(0,0) #a2 = 0 , b2 = 0  """  

#Pre-defined functions 

#1. print()
"""album_rating = [10.0, 8.9, 9, 1, 4, 5, 7.0, 6.9]
print(album_rating)

#2. sum()
print( sum (album_rating))

#3. len()
print (len (album_rating))
"""

#In-Built functions
#In Python, an in-built function is a pre-defined function that is always available for use, providing common functionality without requiring any imports

#Sum of tuple
"""a = (1,2)
c = sum (a)
print(f"The sum of the element in the tuple {a} is {c}")
"""
#Sum of list
"""a = [1,2]
c = sum (a)
print(f"The sum of the element in the list {a} is {c}")
"""

#Using if/else Statements and Loops in Functions
def type_of_album(album_name, released_year):
    print(album_name, released_year)

    if released_year > 1890 :
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("The BodyGuard", 1980)  
print(x)


#Loop in function 
def printList(the_list):
    for element in the_list:
        print(element)

printList([1,'3','The man', 'abc'])


#String comparison in Functions
#Compare Two Strings Directly using in operator
string = "The bodyguard"

def check_string(text):
    if text == string:
        return "String match"
    else : 
        return "String did not match"
    
print(check_string("The bodyguard") )


#Compare two strings using == operator and function

def compareStrings(x,y):
    if x==y:
        return 1

string1 =  "The BodyGuard is the best album"
string2 =  "The BodyGuard is the best album"

check = compareStrings(string1, string2)

if check == 1:
    print("String Matched")
else:
    print("String did not matched")    


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


#Setting default argument values in custom functions
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


isGoodRating(10)        