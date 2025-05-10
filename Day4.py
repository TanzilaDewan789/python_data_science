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


#Quiz on Dictionaries
"""1.Create simple dictionary name soundtrack_dic on- The Bodyguard release 1992, Saturday Night Fever released 1977
a) In the dictionary soundtrack_dic what are the keys ?
b) In the dictionary soundtrack_dic what are the values ?
"""
soundtrack_dic={"The Bodyguard":1992,
                "Saturday Night Fever": 1977}
print(soundtrack_dic)
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

"""2.The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively
a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.
b) Use the dictionary to find the total sales of Thriller:
c) Find the names of the albums from the dictionary using the method keys():
d) Find the values of the recording sales from the dictionary using the method values:"""

album_sales_dict ={'Back in Black':50,
                   "The Bodyguard ":50,
                  "Thriller":65 }
print(album_sales_dict)
print(album_sales_dict["Thriller"])
print(album_sales_dict.keys())
print(album_sales_dict.values())

