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
"""album_year=int(input("whats the album year release year? "))
if(album_year>1980):
    print("Album year is greater than 1980")
elif(album_year==1980):
    print("album was release in year 1980")
else:
    print("Less then 1980")

print("release something new")
"""

#Logical operators
"""Sometimes you want to check more than one condition at once. For example, you might want to check if one condition and another condition are both True. Logical operators allow you to combine or modify conditions.
There are three types of logical operation-
1.and-only when A&B both are true result is true
2.or-only when A&B both are false result is false
3.not- invert the input"""

#Logical operation conditional statement-
#1(AND)
"""album_year= int (input("enter album year"))
if (album_year>1979) and (album_year<1990):#true & true = true
    print("Album year was in between 1980 and 1989")
else:
    print("not found")"""

#2.(OR)
"""album_year =int (input("Your album year: "))
if (album_year<1980) or(album_year>1989):
    print("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")"""

#3.NOT
"""album_year = int(input("album year ? "))
if not (album_year == 1984):
    print("Album year is not 1984")
"""
#Quiz
#1.check if a player Lionel Messi has more than 10 achievements. If the condition is true, print the player's name, sport, and achievements else print does not have more than 10 achievements.
player_name = "Lionel Messi"
sport = "Soccer"
achievements = 12

if achievements > 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")

#2.check if a player belongs to the sport Tennis or has exactly 20 achievements. If the condition is true, print a success message.
player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" or achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")

