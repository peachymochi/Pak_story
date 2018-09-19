"""NEW TOPIC: Write the same block of code in a function and call that function 10 times"""
def EvenOdd():#insert directions below
    import random
    acc = 0
    for i in range (10):
        j = random.randint (0,100)
        if (j%2 == 0):
            print("The number " + str(j) + " is EVEN.")
            acc +=1 #This is the same as "acc = acc + 1"
        else:
            print("The number " + str(j) + " is ODD.")
    print ("The number of EVENS was " + str(acc))


def greeting():
    x = input("Hi, what's your name?: ")
    print ("Hello " + x)
    
def age():
    p = int(input("How old are you?: "))
    return p
    
EvenOdd() #This is "calling" a function
greeting()
age ()