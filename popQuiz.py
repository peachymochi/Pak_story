"""1. Print out a random number between -5 and 5"""
import random
x = random.randint (-5,5)
print (x)

"""2. Print out a random integer between 0 and 100 five hundred times."""
for i in range (500):
    y = random.randint (-5,5)
    print (y)
    
"""3. Print a random number and determine if it is even or odd."""
g = random.randint (0,100)
if (g%2 == 0):
    print("The number " + str(g) + " is EVEN.")
else:
    print("The number " + str(g) + " is ODD.")

"""4. Print 10 random numbers and determine if they are even or odd along the way"""
for i in range (10):
    j = random.randint (0,100)
    if (j%2 == 0):
        print("The number " + str(j) + " is EVEN.")
    else:
        print("The number " + str(j) + " is ODD.")

"""5. Modify the code in part 4 that will ADD up the number of EVEN numbers and print that result. ***Hint: Use an accumulator Variable***"""
acc = 0
for i in range (10):
    j = random.randint (0,100)
    if (j%2 == 0):
        print("The number " + str(j) + " is EVEN.")
        acc +=1 #This is the same as "acc = acc + 1"
    else:
        print("The number " + str(j) + " is ODD.")
print ("The number of EVENS was " + str(acc))


