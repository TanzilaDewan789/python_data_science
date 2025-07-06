#creating a list
person = {
    "name": "Tanzila Dewan",
    "age":24,
    "city":'NY'
}
print(person)

#Accessing Values
print(person["name"]) 

#Add or modify
person['country']= 'USA' # A new entry will be created.
person["city"]='Chicago'  # Update the existing value for the same key
print(person)
#update()
person.update({"Profession": "Engineer"})

#delete
del person["country"]
print(person)

#key existence
print('name' in person)

#Restore/copy()
person = person.copy()
print(person)

#keys()
print(person.keys())
print(list(person.keys()))#keys in list form

#values()
print(person.values())
print(list(person.values()))#values in list form
