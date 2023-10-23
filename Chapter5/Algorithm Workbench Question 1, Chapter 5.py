# Algorithm Workbench Question 1

#Create the function header needed to complete the problem

def times_ten(num): #num is the argument being passed into the parameter
    result = num * 10 #result is the core piece of this function, multiplying the user result by ten
    print(f"The result of the number inputted times ten is: {result}")

num = int(input("What number do you want to put into here?"))
times_ten(num) #Function Call