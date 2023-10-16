#Algorithm Chapter 3, Problem 5. This is the program that will verify the greater number

#The user is able to input numbers and will have the program determine the result

amount1 = int(input("What is the value you want for this?"))
amount2 = int(input("What is the value that you want to put for this?"))

if amount1 > 10: #This verifies that the first condition of the problem, that the first number is greater than 10, is satisfied.
    if amount2 < 100: #This verifies that the second condition of the problem, that the second number is greater than 100, is satisfied.
        if amount1 > amount2: #If amount 1 is greater than amount 2, the first amount will be posted on the console.
            print('The greater value is amount 1:', amount1)
        else: #If amount 2 is greater, then the second amount will be posted.
            print("The greater value is amount 2:", amount2)
    else: #Error handling. This invalidates any inputs that are above 100
        print("amount2 is not less than 100")
else: #This invalidates any inputs that are below 10.
    print("amount1 is not greater than 10")
