"""
Tuple is coolection which is ordered and unchangeable, used to group together related data
"""
student = ("Toheeb", 23, "M")

student.count("Toheeb")#To get the number of time item apear
student.index("M")#To get the position which item is

#Checking if item exist
if "Toheeb" in student:
    print("Toheeb is a name")