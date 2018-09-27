"""
Write a program that defines a function called addSix(n): 
This program should take in a number from the user and then call the function to add six to that number, and then RETURN this number back.
Use the necessary comments and print statements in your code.
"""
def addSix(n):
    print ("You're number " + str(n) + " plus six is " +str(n+6))
    return n
    
n = int(input("Please enter a number and I'll add six to it: "))    
 
addSix(n)
