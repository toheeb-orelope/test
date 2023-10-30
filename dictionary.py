"""
Dictionary: A changeable, unordered collection of unique key:value pairs.
            Fast because they use hashing, allow us to access a value quickly
"""

visitedCountriesm = {"UAE": "Abu Dhabi", "UK": "London", "Turky": "Ankara", "Saudi Arabia" : "Riyadh"}
print(visitedCountriesm["UAE"])#This will print the value of this key
print(visitedCountriesm.get("UK"))#This will return the value and if is not exist it'll not crash our code
print(visitedCountriesm.items())#Print both keys and values

#Loop to print both keys and values
for keys2, values2 in visitedCountriesm.items():
    print(keys2, values2)

key = visitedCountriesm.keys()
print(key)

value = visitedCountriesm.values()
print(value)
print("Stopped here")


visitedCountriesm.update({"Nigeria": "Lagos"})
print(visitedCountriesm)

visitedCountriesm.pop("Nigeria")#This will remove item specified
print(visitedCountriesm)

visitedCountriesm.clear()#This will remove all items in dictionary
