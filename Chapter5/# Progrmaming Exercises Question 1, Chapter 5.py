# Progrmaming Exercises Question 1, Chapter 5

# Kilometer Converter: Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles.

# In order to complete this exercise, we must ask ourselves the formula that is used to convert the units

# This is done by the formula Miles = Kilometers * 0.6214

# Using functions, the program becomes easier to write
km = float(input("How long is the distance in kilometers?"))

def km_to_mi(km):
    miles = km * 0.6214
    print(f"It is {miles} miles away")

km_to_mi(km)
