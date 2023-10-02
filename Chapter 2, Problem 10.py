# Each ingredient is pre-defined. The left number is the number of cups needed to create a batch of 48 cookies.
sugarAmount = 1.5 / 48
butterAmount = 1 / 48
flourAmount = 2.75 / 48

# User is then given a prompt to ask the program how many cookies they would like to make.
cookies = int(input("Fire up those ovens! How many cookies are we going to make today?"))

# Program then takes the quotient of the upper variables, and multiplies them by the number of cookies the user wants to make.
sugarRequired = sugarAmount * cookies
butterRequired = butterAmount * cookies
flourRequired = flourAmount * cookies

# Program outputs the result of the math.
print(f"To make the number of cookies you want,{cookies}, you will need...")
print(f"Look at that Jack! You will need {sugarRequired} cups of sweet sweet sugar to make this happen!")
print(f"Don't slip! You will need {butterRequired} cups of dairy fat-I mean butter to make this all possible!")
print(f"For the foundation of your wonderful cookies, you will need {flourRequired} cups of flour to make this happen!")

