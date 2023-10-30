"""
Set: is collection which is unordered, uninedexed. No duplicate values
"""

kitchenSet = {"Knife", "Spoon", "Fork"}
kitchenSet2 = {"Bowl", "plate", "cup", "Fork"}

#kitchenSet.add("Kitchenroll")#Add item to set
#kitchenSet.remove("Fork")#Remove item
#kitchenSet.clear()#Emypt the set
#kitchenSet.update(kitchenSet2)#This is to add one set to another
#setTable = kitchenSet.union(kitchenSet2)#This is to join one set to another
"""
for kitchen in kitchenSet:
    print(kitchen)
 """
#print(kitchenSet2.difference(kitchenSet))#Get different item which are not in other set
print(kitchenSet2.intersection(kitchenSet))#Get common item in both set