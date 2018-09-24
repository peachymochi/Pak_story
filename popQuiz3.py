"""
Pop Quiz: Use a FOR loop for the following program.

Level 1: 
Write a computer program that will count down from 10.

Level 2: 
Modify the program so that it will count down from whatever number the user decides.

Level 3: 
Modify the program so that it delays 1 second using the package "time" and the method time.sleep(1) inside the loop.
"""
import time

#Level 1:
for i in range (10,-1,-1):
    time.sleep(1)
    print (i)

#Level 2:
x = input("Please enter a number and I will count down to 0 from it: ")
for x in range (int(x),-1,-1):
    time.sleep(1)
    print (x)
    