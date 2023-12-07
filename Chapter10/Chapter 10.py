# Write a class named Car. It accepts 3 data attributes and has 3 methods. 

# The Car class should have an __init__ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s __year_model and __make data attributes. It should also assign 0 to the __speed data attribute.

# Next, design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method, get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.

import time # The time library is imported into the program, this will be relevant later.

class Car(): # Class is defined 
    def __init__(self, year_model, make, speed): # Constructor creates the data attributes, with them being passed as arguments.
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
        
    def set_speed(self): # This sets the speed to a default of zero.
        self.__speed = 0
        
    def get_speed(self): # This simply accesses the speed and helps display the speed to console.
        return self.__speed
    
    def accelerate(self): # This adds a continuous amount of 5.
        self.__speed += 5
    
    def brake(self): # This subtracts a continous amount of 5.
        self.__speed -= 5
        
        
def main():
    
    year_model = int(input("What is the model year of your vehicle?: "))
    make = str(input("What is the make of your vehicle?: ")).strip().lower()
    speed = int(input("What is the current speed of your vehicle?: "))
    
    car_type = Car(year_model, make, speed)
    
    for _ in range(5):
        car_type.accelerate()
        time.sleep(2)
        
        print("Current Speed is...", car_type.get_speed())
        
    for _ in range(5):
        car_type.brake()
        time.sleep(2)
        
        print("Current Speed is...", car_type.get_speed())
    
if __name__ == "__main__":
        main()