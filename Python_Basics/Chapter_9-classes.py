#----------------------------------------------------------------------------Classes------------------------------------------------------------------------
#Classes represent real world things and situations. Objects are created based on these classes.
print("Let's create a class!")

class Dog:

	def __init__(self, name, age): #The self parameter is required. Python uses this parameter automatically when it calls the method later on. 
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")


#A function that part of a class is called a method. The __init__() method is a special method that Python runs automatically whenever we create a new 
#instances based on the Dog class.

print("\nLet's make an instances using the dog class!")

my_dog = Dog('Charlie', 2)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

#If you noticed in order to access the attribute we utilize the dot (.) followed by the attribute. EX: my_dog.name

print("\nLet's call the methods we created with the class!")

my_dog.sit()
my_dog.roll_over()

print("\nLet's create another instance!")
your_dog = Dog('Lucy', 9)

print(f"Your dog's name is {your_dog.name}.")
print(f"You dog's age is {your_dog.age}.")
your_dog.sit()
your_dog.roll_over()

print("\nLet's create our own class!\n")

class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant I want to go to is {self.restaurant_name}.")
		print(f"{self.restaurant_name} serves {self.cuisine_type} food!")

	def open_restaurant(self):
		print(f"{self.restaurant_name} opens at 5PM!")


my_favorite_restaurant = Restaurant('Olive Garden', 'Italian')

my_favorite_restaurant.describe_restaurant()
my_favorite_restaurant.open_restaurant()

your_favorite_restaurant = Restaurant('Del Rican', 'Puerto Rican')

your_favorite_restaurant.describe_restaurant()
your_favorite_restaurant.open_restaurant()

print("\n\nLet's create a car class!\n")

#class Car:
#
#	def __init__(self, make, model, year):
#		self.make = make
#		self.model = model
#		self.year = year
#
#	def get_descriptive_name(self):
#		long_name = f"{self.year} {self.make} {self.model}"
#		return long_name.title()


print("Let's set a default value in our attribute!")
#class Car:
#
#	def __init__(self, make, model, year):
#		self.make = make
#		self.model = model
#		self.year = year
#		self.odometer_reading = 0
#
#	def get_descriptive_name(self):
#		long_name = f"{self.year} {self.make} {self.model}"
#		return long_name.title()
#
#	def read_odometer(self):
#		print(f"This car has {self.odometer_reading} miles on it.")
#
#my_new_car = Car('audi', 'a4', '2019')
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

print("\n\nWe can update this attribute directly by adding the following line: my_new_car.odometer_reading = 'value'")

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

print("\nWe can also modify the attribute by creating a new method!")

#class Car:
#
#	def __init__(self, make, model, year):
#		self.make = make
#		self.model = model
#		self.year = year
#		self.odometer_reading = 0
#
#	def get_descriptive_name(self):
#		long_name = f"{self.year} {self.make} {self.model}"
#		return long_name.title()
#
#	def read_odometer(self):
#		print(f"This car has {self.odometer_reading} miles on it.")
#
#	def update_odometer(self, mileage):
#		self.odometer_reading = mileage

#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

print("\nWe can also ensure the method adds more functionality!")


class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		self.tank_size = 30

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:	
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles
		print(f"This car now has {self.odometer_reading}")

	def fill_gas_tank(self, current_tank):
		if current_tank < self.tank_size:
			needed_tank = self.tank_size - current_tank
			print(f"This car needs {needed_tank} gallons")


#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()


print("\nWe can also create a method that will increment a value as well.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print("\nLet's talk about my old car!\n")

my_used_car = Car('honda', 'accord', 2004)
print(f"My old car is a {my_used_car.get_descriptive_name()}")
my_used_car.update_odometer(12_300)
my_used_car.read_odometer()

print(f"Today, I drove my {my_used_car.get_descriptive_name()} 400 miles.")
my_used_car.increment_odometer(400)
my_used_car.fill_gas_tank(13)

#--------------------------------------------------------------------------Inheritance----------------------------------------------------------------------
#To create a child class we must first have the parent class somewhere above the child class in order to call it properly.
print("\n\nLet's create a child process for electric cars!\n")
#We must specify the parent class in the parentheses
#class ElectricCar(Car):
#We'll create the init for the child process.
#	def __init__(self, make, model, year):
#The super(). allows us to call for methods from the parent class and using the .__init__ allows us to call all attributes.
#		super().__init__(make, model, year)
#Now that we have initialized the parent class' attributes we can now add our own child attributes
#		self.battery_size = 75 

#	def describe_battery(self):
#		print(f"This car has a {self.battery_size}-kWh battery!")
#Previously we had a filled_gas on our parent class but since electric cars don't require gas we can overwrite this attribute.
#	def fill_gas_tank(self):
#		print("This car doesn't need a gas tank")


#my_tesla = ElectricCar('tesla', 'model y', 2022)
#print(f"I now have a {my_tesla.get_descriptive_name()}!")
#my_tesla.describe_battery()
#my_tesla.fill_gas_tank()

#Sometimes certain details may require so much information that they can become a class of their own. 
print("\nLet's make a child class for the battery of an electric car!\n")

#This class will come before our ElectricCar class and it won't inherit any attributes
class Battery:
#We'll define a default battery size
	def __init__(self, battery_size=75):
		self.battery_size = battery_size
#Here's a method that will print the battery size when called
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_distance(self):
		if self.battery_size == 75:
			distance = 260
		elif self.battery_size == 100:
			distance = 315

		print(f"This car can go about {distance} miles on a full charge.") 

class ElectricCar(Car):

	def __init__(self, make, model, year):

		super().__init__(make, model, year)
#Now can call the attributes from the Battery class
		self.battery = Battery() 

	def fill_gas_tank(self):
		print("This car doesn't need a gas tank")


my_tesla = ElectricCar('tesla', 'model y', 2022)
print(f"I now have a {my_tesla.get_descriptive_name()}!")
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_distance()















