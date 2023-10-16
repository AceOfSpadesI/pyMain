#Question 16, February Days

#Create the input field

user_input = int(input("Check how many days in February this year has!: "))

#If conditional is utilized to determine the year's days in February.

#According to the rules set out by the Gregorian Calendar, there are rules regarding a year's apportionment of February days in order to ensure the calendar is stable with the seasons.

#If a year is divisible by 4, it is a leap year.
#If a year is divisible by 100, it is not a leap year.
#If a year is divisible by 400, it is a leap year.

#The % symbol is the remainder symbol. If the remainder of the division problem is not equal to zero (4 and 400 results), then the program goes to the else statement.

#However, for determining the result of 100, it must not be set to zero as without the not operand the program will assume that those years have leap years.

if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0):
    days = 29
else:
    days = 28

print(f"In {user_input}, February has {days} days.")