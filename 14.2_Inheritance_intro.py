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
        self.odometer_reading = mileage

    
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):        #*Child Class(while inheritance you have to include the parent class inside paranthesis)   
    def __init__(self,make,model,year):      #*__init__ takes required info from parent class 
        super().__init__(make,model,year)    #*super() allows the child class to call a "method" from parent class
        self.battery_size = 75    #*defining new attributes for child class

myTesla = ElectricCar('tesla', 'model S', '2019')
print (myTesla.get_name())
print (f"This car has a {myTesla.battery_size}-kWh battery.")


