#Task-1 Create an empty list
Shopping_list=[]


"""Task-2 Now store the number of items to the shopping_list
Watch
Laptop
Shoes
Pen
Clothes"""
Shopping_list=["Watch",'Laptop','Shoes','Pen','Clothes']

"""Task-3 Add a new item to the shopping_list
Seems like I missed one item "Football" to add in the shopping list."""
Shopping_list.append("Football")
print(Shopping_list)


#Task-4 Print First item from the shopping_list
print(Shopping_list[0])

#Task-5 Print Last item from the shopping_list
print(Shopping_list[-1])#negative indexing start from right to left and from -1,-2,-3,-...

#Task-6 Print the entire Shopping List
print(Shopping_list)

"""Task-7 Print the item that are important to buy from the Shopping List
Print "Laptop" and "shoes"""
print(Shopping_list[1:3])

"""Task-8 Change the item from the shopping_list
Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list."""
Shopping_list[3]='Notebook'
print(Shopping_list)

"""Task-9 Delete the item from the shopping_list that is not required
Let's delete items that are unimportant, such as; I don't want to buy Clothes, let's delete it."""
del(Shopping_list[4])
print(Shopping_list)

"""Task-10 Print the shopping list
We are ready with our shopping list."""
print(Shopping_list)