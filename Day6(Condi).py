"""Comparison Operators
Comparison operations compare some value or operand and based on a condition, produce a Boolean. When comparing two values you can use these operators:

1.equal: ==
2.not equal: !=
3.greater than: >
4.less than: <
5.greater than or equal to: >=
6.less than or equal to: <="""

#1. 
a=6
if (a==5):
    print('True')

else:
    print('False')    

#2.
b=4
if(b!=4):
    print('False')

else:
     print('True')

# Use Equality sign to compare the strings
value = 'AC/DC'
if(value=="The bodyguard"):
    print("True")
else: 
    print("False")    

# Compare characters
value1 = 'B'
if(value1>"A"):
    print('true')
else: 
    print("false") # Ascii:- A=65, B=66
# Compare characters  by multiplication

Multi = 'BA'
if(Multi>"AB"):
    print('true')
else: 
    print("false") 

#Branching
#Branching allows us to run different statements for different inputs. 


#1. If statement example
"""age = 19
if (age > 18):    
    print("you can enter" )
print("move on")
"""


#2. Else statement example
"""age1 = int (input("How old are you?"))
if (age1 >18):
    print("you can enter")
else:
    print("go see Meat Loaf")

print("Move on") """   

#3.Elif statement example
"""age2 = int(input("Tell me your age: "))
if (age2>18):
    print("You can enter")
elif (age2==18):
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")

print("Move on")"""

#4.Condition statement example- take album year and print if its greater then 1980 or not
album_year=int(input("whats the album year release year? "))
if(album_year>1980):
    print("Album year is greater than 1980")
elif(album_year==1980):
    print("album was release in year 1980")
else:
    print("Less then 1980")

print("release something new")

