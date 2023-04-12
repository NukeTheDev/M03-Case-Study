import os

# Program name:       Car Attribute entry system
# Author:             Charles Phillips
# Version:            version 1.0
# Last revision date: 04/11/2023
# The objective of this program is to prompt a user to enter the demographics of a car such as year, make and model,
# , Whether it is a coupe (2 door) or a 4-door (sedan)
# Finally, it presents this data in an easy to read form

#Superclass that contain an attribute for vehicle type."
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# regular class called Automobile which will inherit the attributes from Vehicle such as year, make and model of the vehicle.
class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None

    def get_vehicle_details(self):
        """
        Prompts the user to input the car's details and stores them in the corresponding attributes of the Automobile object.
        """
        while True:
            try:
                self.year = int(input("Enter the year of the car: "))
                break
            except ValueError:
                print("Please enter a valid integer for the year.")
                
                
        self.make = input("Enter the make of the car: ")
        while self.make.isalpha() != 1:  # User input validation
            self.make = input("Invalid car make!', 'Please enter only letters (string)")
        os.system('cls')
        
        self.model = input("Enter the model of the car: ")
        while self.model.isalpha() != 1:  # User input validation
            self.model = input("Invalid model name!', 'Please enter only letters (string)")
        os.system('cls')
        
        while True:
            try:
                self.doors = int(input("Enter the number of doors (2 or 4): "))
                if self.doors not in [2, 4]:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid integer for the number of doors (2 or 4).")
        
        while True:
            self.roof = input("Enter the type of roof (solid or sun roof): ")
            if self.roof not in ["solid", "sun roof"]:
                print("Please enter a valid roof type (solid or sun roof).")
            else:
                break

    #Function that Prints out the car's details in a readable format."
    def display_vehicle_details(self):
        """
        """
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# main program
car = Automobile("car")
car.get_vehicle_details()
print("\nCar Details:")
car.display_vehicle_details()