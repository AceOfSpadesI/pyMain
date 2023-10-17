# Algorithm Workbench Problem 2

#I had ChatGPT help me out with this one. While loops were a bit of a challenge for me to understand at first but I get them now
while True:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    # Calculate and display the value
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")
    # Ask if the user if they want to repeat the operation
    repeat = input("Do you want to perform the operation again? (yes/no)")
    # If the answer is anything but yes, break the function
    if repeat != "yes":
        break