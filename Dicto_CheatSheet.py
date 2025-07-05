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
person["city"]='Manchester'  # Update the existing value for the same key
print(person)