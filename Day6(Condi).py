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

# If statement example:-1

age = 19
#age = 18

#expression that can be true or false
if (age > 18):
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

#2
