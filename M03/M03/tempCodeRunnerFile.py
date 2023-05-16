An app that will accept user input for a car.
The app will store "car" into the vehicle type in Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes.
The app will then output the data in an easy-to-read and understandable format:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
"""

#A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
class Vehicle():
    def __init__(self,vehicle_type) :
        self.vehicle_type = vehicle_type
        

#A class called Automobile   
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)    # inherit the attributes from Vehicle
        self.year = year                  # contain the following attributes:
        self.make = make
        self.model = model
        self.doors = doors                # doors (2 or 4)
        self.roof = roof                  # roof (solid or sun roof)

car = Automobile(input("What type of vehicle? :"),
    input( "What year was the vehicle made? :"),
    input( "What is the make of the vehicle? :"),
    input( "What is the model of vehicle? :"),
    input( "How many doors does the vehicle have? :"),
    input( "Is the roof 'solid' or 'sun roof'? :"))

print(f"""
    Vehicle type: {car.vehicle_type} 
    Year: {car.year}
    Make: {car.make}
    Model: {car.model}
    Number of doors: {car.doors}
    Type of roof: {car.roof}
     """ )
