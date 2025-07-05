#Creating a Dictionary
person = {
    "name": "Jhone",
    "age" : 24,
    "city":"NY"
}
print(person)

#Accessing Values
print(person.values())
#Add/Modify
person['University']= 'MIT'
#Delete
del(person["city"])
print(person)

