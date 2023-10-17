# Programming Exercise 1, Bug Collector

bugs = 0 # The variable bugs has to be set to zero

for day in range(1, 6): # For every day within the 1 to 6 range (Python uses a zero index, so all are off by one, making it 0 through 5), add the bugs collected
    collected_bugs = int(input("How many bugs did you collect today?"))
    bugs += collected_bugs # Once the variables are set, the += operator adds all the variables up.

print(f"{bugs} bugs have been collected over five days") # Print the result