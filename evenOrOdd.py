"""
Write a program that will take a number (Integers only) and return a statement that will let the user know if it is even or odd
"""

x=float(input("Please enter a number (Integer Please): "))

if (x%2 == 0):
    print ("This number is even.")
    
elif (x%2 == 1):
    print ("This number is odd.")
    
else:
    print ("This is not an integer.")