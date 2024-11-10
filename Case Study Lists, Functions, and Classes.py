# This app is designed to gather automobile information from the user\
# Xavier Randolph
# Define the superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type  

# Define the subclass Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main function to run the app
def main():
    # Ask the user for the car details
    print("Let's gather information about your car!")

    
    vehicle_type = "car"

    # Get other information from the user
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    
    automobile = Automobile(vehicle_type, year, make, model, doors, roof)

   
    print("\nVehicle Information:")
    automobile.display_info()

if __name__ == "__main__":
    main()
