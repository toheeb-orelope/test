"""
List is used to store multiple items in a single variable
"""

food = ["Banana", "Yam", "Beef", "Hams"]#List declaration

#Update a list
food[1] = "Potato"
#Print updated version

food.append("Mango")#Add item at the end
#food.clear()#Delete everything in the list
food.pop()#Remove item from the end
food.count()#Count the items in the list
food.extend()#Extend the list
food.remove("Beef")#Remove item at specified index
food.insert(2, "Beef")#Add item at the given location
