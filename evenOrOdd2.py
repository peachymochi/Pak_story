"""
Write a program that will ask the user for a number (Integers only) and return a statement that the number is EVEN or ODD.
"""
num = int(input("Please type in a number (Integer only please): "))
if (num%2 == 0):
    print ("The number " + str(num) + " is even.")
    
else:
    print ("The number " + str(num) + " is odd.")