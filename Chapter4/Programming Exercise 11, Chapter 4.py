# Programming Exercise 11, Chapter 4

weight = int(input("Starting weight here: ")) # User input

print("Weight\tMonth") # Creating a header

losing_weight = weight # Initalize the already declared variable with a new variable

for month in range (1, 7): # Loop is set for 6 months
    losing_weight -= 4 # You are losing 4 pounds
    print(f"{month}\t{losing_weight} pounds") # Print the result of the calculation

print(f"Total weight lost in 6 months is {losing_weight} pounds") # Print the final result