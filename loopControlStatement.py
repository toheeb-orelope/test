"""
Loop control statement: Change a loops excustion from its normal sequence

1. break: Used to terminate the loop entirely
2. continue: Skips to the next iteration of the loop
3. pass: Does nothing, acts as a placeholder
"""

#Break
"""
while True: 
    name = input("What is your name: ")
    if name != "":
        break
print(f"Your name is {name}")"""

#Continue
"""
phoneNumber = "123-6545-3846"
for number in phoneNumber:
    if number == "-":
        continue
    print(number, end="")"""

#Pass
for number in range(1, 23):
    if number == 3:
        pass
    else:
        print(number, end="")