"""
Nested loops: The inner loop will finish all of it's iteration before
                finishing one iteration of the outer loop
"""
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("What is your favorit symbol: ")

#Outer loop to control the number of rows 
for outloop in range(rows):
    #Inner loop to control the number of columns
    for innerloop in range(columns):
        print(symbol, end="")#Print the symbol
    #print empty space to control between the iteration
    print()