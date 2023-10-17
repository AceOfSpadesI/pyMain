#Algorithm Workbench, Question 1


#Product, as defined in the problem, has to be set to zero in order for the loop to work.
product = 0
#Create the user input.
user_input = int(input("Number you want multiplied here: "))
#While loop executes the function until the number hits 100
while product < 100:
    product = user_input * 10
#Print result
print(product)
