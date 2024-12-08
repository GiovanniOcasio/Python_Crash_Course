from car import Car

class Battery:

	def __init__(self, battery_size=75):
		self.battery_size = battery_size

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
