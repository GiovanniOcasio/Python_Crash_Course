#---------------------------------------------------------------------------If Statements---------------------------------------------------------------------
#If statements are conditional statements that execute if certain conditions are met
print("Here is a simple example of a if statement")

cars = ['audi', 'bmw', 'honda', 'chevy', 'camery']

for car in cars:
	if car == 'honda':
		print(car.upper())
	else:
		print(car.title())

print("Here we stated if the car value was honda it would print with the .upper method. Anything else would print with the .title method")

#----------------------------------------------------------------------Conditional Statements---------------------------------------------------------------
#The if statement uses True and False values as a conditional test. For example, above the conditional test or Boolean expressionis whether car is equal to 'honda' using the
#equality operator (==). Also, the equality operator is case sensitive. We can also use the if statement with the inequality operator(!=).
print("\n\nLet's create an if statement using the inequality operator (!=)")

for car in cars:
	if car != 'bmw':
		print(f"This {car.title()} isn't mine!")
	else:
		print(f"Thanks for getting my {car.upper()}!")

#We can also use multiple conditions with an if statement, such as greater than or equal to(>=), less than or equal to(<=), less than(<), 
#greater than(>), etc. using the 'and' keyword.
print("\n\nLet's set a variable stating old age is equal to 65 and the young age as 18")

old_age = 65
young_age = 18
my_age = 27

if my_age <= old_age and my_age >= young_age:
	print("You aren't that old.")
else:
	print("Wow you're that old!")

#------------------------------------------------------------------Checking For an Item In a List-----------------------------------------------------------
#You can use the 'in' and 'not in' keywords to check for elements in a list.
print("\n\nLet's use the cars list to check if certain values are in or not in the list")

favorite_car = "lamborghini"
print(f"My favorite car is a {favorite_car.title()}")

if favorite_car in cars:
	print("This list has my favorite car!")

print("\nWe can check if my favorite car isn't the cars list.")
if favorite_car not in cars:
	print("Hey, my favorite car isn't on this list!")

#---------------------------------------------------------------------------If Elif Else---------------------------------------------------------------------
#We have worked with simple if statements, if-else statements, now let's work with if-elif-else statements. This will run each boolean test in order until 
#one passes.
print("\n\nLet's create an if-elif-else statement where we'll determine admission cost based on the my_age vaiable specified earlier.")

if my_age < 4:
	print("Your admission is free!")
elif my_age < 18:
	print("Your admission is $20.")
else:
	print("Your admission is $35.")

#-------------------------------------------------------------------Multiple If Elif Else--------------------------------------------------------------------
print("\n\nLet's create an if-elif-else with multiple elif statements.")

if my_age < 4:
	print("Your admission is free!")
elif my_age < 18:
	print("Your admission is $20.")
elif my_age < 50:
	print("Your admission is $40.")
else:
	print("Your admission is $25.")

print("\nWe can also omit the else statement and just end the statements with elif.")

if my_age < 4:
	price = "$0"
elif my_age < 18:
	price = "$20"
elif my_age < 50:
	price = "$40"
elif my_age > 50:
	price = "$25"

print(f"Your admission will cost {price}")

#If-Elif-Else statements are only usable in situations where only one statements needs to pass.

#--------------------------------------------------------------Combining If Elif Else With Loops-------------------------------------------------------------
#Let's combine if-elif-else statements with a for loop
toppings = ['mushrooms', 'pepperoni', 'bacon', 'ham', 'extra cheese']
requested_toppings = ['pepperoni', 'bacon', 'green peppers']

print(f"The customer has requested the following toppings: {requested_toppings}")

for requested_topping in requested_toppings:
	if requested_topping in toppings:
		print(f"Adding {requested_topping}")
	elif requested_topping not in toppings:
		print(f"Sorry, we do not have {requested_topping}")


#---------------------------------------------------------------------------Chapter Lab---------------------------------------------------------------------
print("\n\nChapter Lab")
usernames = ['admin', 'amado.a', 'lisa.c', 'mateo.m', 'rio.c', 'giovanni.o']

for username in usernames:
	if username == 'admin':
		print(f"Welcome back, {username.title()}!")
	elif username != 'admin':
		print(f"Hello, {username.title()} welcome back!")

print("\n\nLet's add new users!")
new_users = ['john.d', 'lilly.o', 'lisa.c', 'tommy.g']

for new_user in new_users:
	if new_user in usernames:
		print(f"Sorry, {new_user.title()} the username {new_user} is taken. Please select another username.")
	elif new_user not in usernames:
		print(f"Welcome {new_user.title()}, you should receive an email to complete registration!")


numbers = list(range(1, 10))
print("\n\nOur number list:", numbers)

for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")


