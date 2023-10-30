"""
indexing[]
slice()
[start: stop: step]
"""
"""
name = "Toheeb Husain"
firstName = name[:5]#Indexing
lastName = name[7:]
funkyName = name[0:12:2]#this will print every 2 letter of each word
reversedName = name[::-1]#This will print from the last letter

print(funkyName)
"""
#Slicing  is to extract words out of the part
website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)

print(website1[slice])
print(website2[slice])