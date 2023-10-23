# Question 18, Chapter 5, Prime Number List

def is_prime(num):
    if num <= 1:
        return False # Numbers that are less than one are not prime because they can be divided by both -1 and 1
    for i in range(2, num):
        if num % i == 0: # If any number can divide the input, it's not prime
            return False
    return True
    
for num in range(1, 101): # For loop cycles through to find any available primes
    if is_prime(num): # If statement calls the function to operate
        print(num, end=" ") # Prints the true results of num and spaces them out with the end parameter





