# User inputs the parameters for the grapevine

user_length = int(input("Input the length of the vineyard here in feet:"))
user_space = int(input("Input the amount of space used in feet by an end post assembly here:"))
user_vines = int(input("Input the space in between the vines in feet here:"))

# Equation that is used in order to calculate the total number of grapevines that would fit

grapevine_total = (user_length - (2 * user_space)) / user_vines

# As Python doesn't automatically round floating points, I added a round function to simplify the final result

rounded_grapevines = round(grapevine_total)

# I added an if statement to create a realistic result for the grapevines, as having negative grapevines makes no sense.

if rounded_grapevines > 0:
    print(f"The number of grapevines that will fit here in the row is {rounded_grapevines}")
if rounded_grapevines < 0:
    print("You can't fit any grapevines here, try again!")

