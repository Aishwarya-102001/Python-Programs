class Car:
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
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

new_car = Car('audi','a4','2019')
print (f"My new car is :", new_car.get_name())

new_car.update_odometer(20)             # Modifying an attribute's value through a method
# new_car.odometer_reading = 23         # Modifying an attribute's value directly
new_car.read_odometer()

new_car.increment_odometer(10)          # Incrementing an attribute's value through a method
new_car.read_odometer()