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

