import time

#Count down time
for second in range(10, 0, -1):
    print(f"The count down starting now: {second}")
    #Timing implementation
    time.sleep(1)#Sleep(1) mean I want it to be start counting down by 1 seconds
print("Happy new year")