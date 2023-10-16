#Question 1, Day of the Week

#Prompts the user with a question to input a number into the program
user_input = int(input("Put in the number for the day of the week."))

#If statement conditional ensures that the appropriate number is given an appropriate result
if 1 <= user_input <= 7:
    if user_input == 1:
        day = "Monday"
    elif user_input == 2:
        day = "Tuesday"
    elif user_input == 3:
        day = "Wednesday"
    elif user_input == 4:
        day = "Thursday"
    elif user_input == 5:
        day = "Friday"
    elif user_input == 6:
        day = "Saturday"
    else:
        day = "Sunday"
else: #Error handling
    print("You didn't put in a number from 1 to 7")

print(day)
