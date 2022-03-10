# from car import Car

# my_new_car = Car('audi','a4',2019)
# print (my_new_car.get_name())

# my_new_car.odometer_reading = 46
# my_new_car.read_odometer()

#*********************Storing multiple classes in a module************************

from car import ElectricCar as EC   #using aliases

my_new_car= EC('tesla','model s',2019)

print(my_new_car.get_name())

my_new_car.battery.describe_battery()


#********************Importing multiple classes from a module**************************

# from car import Car, ElectricCar

# my_bettle = Car('volkswagen','bettle',2019)
# print (my_bettle.get_name())

# my_tesla = ElectricCar('tesla','model s',2019)
# print(my_tesla.get_name())


#********************Importing an entire module**************************

# import car

# my_bettle = car.Car('volkswagen','bettle',2019)   #Syntax:  module_name.ClassName
# print (my_bettle.get_name())

# my_tesla = car.ElectricCar('tesla','model s',2019)
# print(my_tesla.get_name())
