#Programming Exercise 14, Chapter 4

# Define the number of rows for the pattern.
num_rows = 7

# Outer loop for rows.
for i in range(num_rows, 0, -1): #This will loop the rows to always shrink by one character.
    # Inner loop for printing asterisks.
    for j in range(1, i + 1): #This will always print an asterisk until the i for loop no longer can accommodate the j loop printing asterisks.
        print("*", end="")
    print()  # Move to the next line.