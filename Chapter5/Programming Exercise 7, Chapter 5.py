# Programming Exercise 7, Chapter 5

# Create the global variables that are necessary for the program to function.

classA = 20
classB = 15
classC = 10

# Create the function that will use these global variables as arguments
def calc_income(totalA, totalB, totalC):
    income = (totalA * classA) + (totalB * classB) + (totalC * classC)
    return income

def total_amount():
    totalA = int(input("How many Class A tickets were sold?"))
    totalB = int(input("How many Class B tickets were sold?"))
    totalC = int(input("How many Class C tickets were sold?"))
    return totalA, totalB, totalC

def main():
    totalA, totalB, totalC = total_amount()
    income = calc_income(totalA, totalB, totalC)
    print("The total income generated from the ticket sales is: $", income)

if __name__ == "__main__":
    main()
