# Question 17, Prime Numbers

# Question asks whether or not your submittion is in fact a prime number

# This is done by taking the number and defining it's primeness through a function

# Define the function to check a number's primeness
def is_prime(num):
    if num <= 1:
        return False # Numbers that are less than one are not prime because they can be divided by both -1 and 1
    for i in range(2, num):
        if num % i == 0: # If any number can divide the input, it's not prime
            return False
    return True
    
user_input = int(input("Enter a number: ")) # Get user input

if is_prime(user_input): # Print the results
    print(f"{user_input} is a prime number")
else:
    print("It's not a prime number!")