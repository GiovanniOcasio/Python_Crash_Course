#------------------------------------------------------------------------Importing Classes------------------------------------------------------------------
#Similar to how we imported functions we can also import classes.
#from car import Car,ElectricCar

#my_audi = Car('audi', 'a4', 2019)
#print(f"{my_audi.get_descriptive_name()}")

#my_audi.odometer_reading = 15
#my_audi.read_odometer()

#my_tesla = ElectricCar('tesla', 'model 3', 2022)
#print(f"{my_tesla.get_descriptive_name()}")
#my_tesla.odometer_reading = 5
#my_tesla.read_odometer()
#my_tesla.battery.get_distance()

print("\nWe can also import the entire module!\n")

#import car

#my_audi = car.Car('audi', 'a4', 2019)
#my_tesla = car.ElectricCar('tesla', 'model 3', 2022)

#print(f"{my_audi.get_descriptive_name()}")
#print(f"{my_tesla.get_descriptive_name()}")

print("\nWe can also import the a module into another module!\n")

#We can also do things like importing modules into another module.
from car import Car
from electric_car import ElectricCar

my_audi = Car('audi', 'a4', 2019)
my_tesla = ElectricCar('tesla', 'model 3', 2022)

print(f"{my_audi.get_descriptive_name()}")
print(f"{my_tesla.get_descriptive_name()}")

#We can also use alias similar to how we did in the functions chapter
#----------------------------------------------------------------------------Functions----------------------------------------------------------------------
