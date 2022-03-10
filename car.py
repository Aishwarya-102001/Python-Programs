class Car:              #**********Parent Class
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0       # setting a default value for an attribute
    
    
    def get_name(self):
        name = f"{self.year} {self.make} {self.model}"
        return name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self,miles):
        self.odometer_reading += miles


#*********************Storing multiple classes in a module***********

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print (f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):        
    def __init__(self,make,model,year):      
        super().__init__(make,model,year)   
        self.battery = Battery()