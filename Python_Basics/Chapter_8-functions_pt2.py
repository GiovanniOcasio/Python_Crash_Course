#------------------------------------------------------------------------Importing Modules------------------------------------------------------------------
#If we have a Python script in the directory our current script is being developed in we can import the script into our current script.
print("We have pizza.py stored in our present directory, which contains the make_pizza function")
#def make_pizza(size, *toppings):
#	print(f"\nMaking a {size}-inch pizza with the following toppings:")
#	for topping in toppings:
#		print(f"- {topping}")
print("\nWe can in use it by using 'import pizza'")

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#Note that we specified the script by using import script name. Then we can use it by specify the module we imported (pizza) and the function we're 
#executing (make_pizza).


#------------------------------------------------------------------Importing Specific Functions-------------------------------------------------------------
#If a module contains several functions, we may want to only import a specific function.

print("\n\nLet's import a function from a module!")

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(14, 'green peppers', 'pepperoni', 'ham')

#----------------------------------------------------------------------Give Modules an Alias----------------------------------------------------------------
print("\n\nLet's give the module we're importing an alias that we can use to call the function!")

import pizza as p

p.make_pizza(18, 'pepperoni', 'ham', 'sausage')

#--------------------------------------------------------------------Importing All Functions----------------------------------------------------------------
#If a module contains several functions, we can choose to import all functions.
print("\n\nLet's use all functions within the pizza module")

from pizza import *

print("\n\nLet's use all functions within the pizza module")

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
formatted_name = greetings(f_name, l_name)
print(f"Welcome, {formatted_name}! Let's get your order!")

make_pizza(18, 'red peppers', 'extra cheese')

input("Hit enter to quit")

