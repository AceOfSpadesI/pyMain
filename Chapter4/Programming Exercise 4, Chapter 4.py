# Get the speed (miles per hour) and the number of hours from the user
speed = float(input("Enter the speed of the vehicle (miles per hour): "))
hours = int(input("Enter the number of hours the vehicle has traveled: "))

# Display a header for the output
print("Hour\tDistance Traveled")

# Initialize a variable to keep track of the total distance
total_distance = 0

# Use a loop to calculate and display the distance for each hour
for hour in range(1, hours + 1):
    distance = speed * hour  # Calculate the distance for the current hour
    total_distance += distance  # Update the total distance
    print(f"{hour}\t{distance:.2f} miles")

# Display the total distance traveled
print(f"Total distance traveled: {total_distance:.2f} miles")