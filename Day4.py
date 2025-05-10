""" What are Dictionaries?
A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary."""
# Create the dictionary
Dict = {"key1":1,
        "key2":"2",
        "key3":(3,3,3),
        "key4":[4,4,4,4],
        'key5':5,
        (0, 1): 6}
print(Dict)


# Access to the value by the key
print(Dict["key3"])
print(Dict[(0, 1)])

release_year= {"Thriller": "1982", 
                    "Back in Black": "1980", 
                    "The Dark Side of the Moon": "1973",
                    "The Bodyguard": "1992", 
                    "Bat Out of Hell": "1977",
                    "Their Greatest Hits (1971-1975)": "1976", 
                    "Saturday Night Fever": "1977", 
                    "Rumours": "1977"}
print(release_year)
print(release_year["The Dark Side of the Moon"])

# Get all the keys in dictionary
print(release_year.keys())

# Get all the values in dictionary
print(release_year.values())

# Append value with key into dictionary{Dictionary is mutable}
release_year["graduation"]='2007'
print(release_year)

# Delete entries by key
del(release_year["Thriller"])
del(release_year["graduation"])
print(release_year)

# Verify the key is in the dictionary
print('The Bodyguard' in release_year)
