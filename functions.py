"""
This is all about how functions work
"""

def greeting():  #This function does NOT return anything
    print ("Hello World")

def askName():
    name = input("What is your name? ")
    return name
    
def askAge():  
    age = int(input("How old are you? "))
    return age

def canVote(age): #Write a function that takes their age IN and responds appropriately if they can or cannot
    if (age >= 18):
        print("You can vote!")
        canVote = True
    else:
        print("Sorry, you can't vote...")
        canVote = False
    return canVote
   


#call the function
greeting()
x = askName() #Save the putput of askName() to variable
print ("Hello " + x)

#call the function and save the age to a variable
y = askAge() #y = age
z = canVote(y) #z = if they can vote or not (T/F)
print (z)