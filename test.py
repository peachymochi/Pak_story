import Quiz2 #Import files from within your own package (repository)

Quiz2.EvenOdd()

Quiz2.greeting()

p = Quiz2.age() #Stores the return value of the function age

if (p >= 18):
    print ("You are old enough to vote.")
else: 
    print ("In " + str(18-p) + " years, you will be able to vote.")
