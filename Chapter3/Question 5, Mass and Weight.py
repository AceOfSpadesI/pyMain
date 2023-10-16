#Question 5, Mass and Weight

#Ask the user for an input

user_input = int(input("Put a weight in kilograms here: "))

#Apply the user input to the equation

newtons = (user_input * 9.8)

#If conditional is used to determine if our number passes the newton weight test

if newtons >= 100 and newtons <= 500:
    print(newtons, "Newtons")
elif newtons < 100:
    print("It's too light!", newtons, "Newtons")
elif newtons > 500:
    print("It's too heavy!", newtons, "Newtons")