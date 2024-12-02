#---------------------------------------------------------------------------Dictionaries--------------------------------------------------------------------
#Dictionaries allow users to connect related information. A dictionary is a collection of key-value pairs, it is typically wrapped in braces '{}' with a 
#series of key-value pairs.
print("Let's create a simple dictionary using an individuals race and age!")

person_1 = {'race': 'hispanic', 'age': 27}

print(person_1['race'])
print(person_1['age'])

print("In this instance the key was race and age, with the values being hispanic and 27.")

user1_race = person_1['race']
user1_age = person_1['age']

print(f"The first user is {user1_race}, and {user1_age} years old!")

#-------------------------------------------------------------------------Adding Information-----------------------------------------------------------------
#We can add information to a dictionary by specifying the dictionary and the information we want to add
print("\n\nLet's add information to the person_1 dictionary")

person_1['eye_color'] = 'brown'
person_1['hair_color'] = 'black'

print(person_1)

#--------------------------------------------------------------------------Empty Dictionary------------------------------------------------------------------
print("\n\nLet's start with an empty dictionary for person_2!")

person_2 = {}

person_2['race'] = 'white'
person_2['age'] = 19
person_2['eye_color'] = 'green'
person_2['hair_color'] = 'brown'

print(person_2)

#-----------------------------------------------------------------------Modifying Dictionary----------------------------------------------------------------
print(f"\n\nLet's see the current eye_color of person_1: {person_1['eye_color']}")

person_1['eye_color'] = 'hazel'

print(f"\nNow the eye_color for person_1 is {person_1['eye_color']}")

#Let's do a more complex example
target_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print("\n\nWe have a target that is located on the top left of the screen now let's move it across using if-elif-else.")

if target_1['speed'] == 'slow':
	x_increment = 1
elif target_1['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

print(f"\nOriginal Position: {target_1['x_position']}")

target_1['x_position'] = target_1['x_position'] + x_increment

print(f"New Position: {target_1['x_position']}")

#------------------------------------------------------------------------Deleting Dictionary----------------------------------------------------------------
print("\n\nLet's delete a key-value pair.")

person_2['specialty'] = 'birthmark'

print(person_2)

del person_2['specialty']

print(person_2)

#---------------------------------------------------------------------Similar Object Dictionary-------------------------------------------------------------
#Previously we created a dictionary on different objects that are related to the item. Now we can create an dictionary of similar objects.
print("\n\nLet's create a dictionary about a groups favorite pizza!")

favorite_pizza = {
	'lisa': 'ham',
	'lilly': 'hawaiian',
	'mateo': 'pepperoni',
	'gio': 'bacon',
	'rio': 'everything'
}

print(favorite_pizza)

pizza = favorite_pizza['lilly'].title()
print(f"Lilly's favorite pizza is {pizza}")

#-----------------------------------------------------------------------Some Errors You May Get-------------------------------------------------------------
#If you request a key-value pair that doesn't exist you'll receive an error. you can use the get() method to set a default value for key.
print("\n\nThe current key-value pair for person_1 is", person_1)
print("There isn't a specialty value like we used to have for person_2, so let's set a default value using get()")

specialty_value = person_1.get('specialty', 'No Specialty Value Assigned')
print(specialty_value)

#-------------------------------------------------------------------Looping Through Key-Value Pairs---------------------------------------------------------
#We can use for loops to go through all the key-value pairs within a dictionary
user_0 = {
	'username': 'a.alifonso',
	'first': 'amado',
	'last': 'alifonso',
	'dob': '11/15/1975',
}

print("\n\nSay we have a new dictionary for user_0", user_0)
print("We can loop through all the key-value pairs, and with the .items() method, we can return a list of items within the dictionary")

#The temporary variables of 'key' and 'value' can be anything but for simplicity we'll use key and value.
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

print("\nLet's loop through the favorite pizza dictionary we crated earlier:")

for name, pizza in favorite_pizza.items():
	print(f"{name.title()}'s favorite pizza is {pizza.title()}.")


#-------------------------------------------------------------------Looping Through All Keys Pairs----------------------------------------------------------
#Using the key() method is useful when we aren't too concerned about the value.
print("\n\nLet's see who participate in the poll with a for loop using the key() method.")

for name in favorite_pizza.keys():
	print(f"{name.title()} took the poll")

coworkers = ['lisa', 'amado', 'rio']

print("\n\nNow let's make a for loop that also contains an if-else statement. This will send a specific message to participants who are also coworkers.")

for name in favorite_pizza.keys():
	if name in coworkers:
		pizza = favorite_pizza[name].title()
		print(f"{name.title()}'s a coworker and took the poll. {name.title()} loves {pizza} pizza!")
	else:
		print(f"{name.title()} isn't a coworker but they took the poll!")

#---------------------------------------------------------------Looping Through All Keys Pairs in Order-----------------------------------------------------
print("\n\nWe can also sort keys permenantly or temporary!")

for name in sorted(favorite_pizza.keys()):
	print(f"{name.title()}, thank you for taking the poll!")

print("\nNow in reverse\n")

for name in reversed(favorite_pizza.keys()):
	print(f"{name.title()}, thank you for taking the poll!")


#-----------------------------------------------------------------Looping Through All Values in Order-------------------------------------------------------
print("\n\nThe following pizza toppings were mentions:")

for pizza in favorite_pizza.values():
	print(f"{pizza.title()}")

#If the list contain several elements of the same value it would print those values. In this case we want the output to be unique values. For this we would
#use the set() method.
favorite_pizza = {
	'lisa': 'ham',
	'lilly': 'hawaiian',
	'mateo': 'pepperoni',
	'gio': 'bacon',
	'rio': 'everything',
	'amado': 'pepperoni',
}

print("\n\nAmado took the survey now we can see his choice.")

for pizza in favorite_pizza.values():
	print(f"{pizza.title()}")

print("\nWe need only unique values so let's use the set() method")

print("\nThese are the unique toppings that were chosen:")

for pizza in set(favorite_pizza.values()):
	print(f"{pizza.title()}")


#-----------------------------------------------------------------------------Nesting-----------------------------------------------------------------------
#We can create dictionaries and store them to a list. This is known as nesting.
print("\n\nLet's create three dictionaries with the description of alien characters. Then, we'll nest these dictionaries into a list.")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(f"This is one kind of alien: {alien}")

print("\nLet's make a longer list of aliens!\n")

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:8]:
	print(alien)

print(f"\nThe total number of aliens are: {len(aliens)}")

print("\nLet's split the aliens into three groups with a for loop and if-elif statement!\n")

for alien in aliens[0:10]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15 

print(aliens[6:12])

#-----------------------------------------------------------------------List in Dictionaries----------------------------------------------------------------
#Sometimes it's more feasible to store a list of elements as a key value in a dictionary
print("\nLet's store a list in a dictionary")

pizza = {
	'crust': 'thick',
	'toppings': ['pepperoni', 'bacon', 'ham', 'green peppers']
}

print(f"You picked the {pizza['crust']} crust and the following toppings")

for topping in pizza['toppings']:
	print(f"{topping}")

favorite_languages = {
	'gio': ['python', 'bash'],
	'lisa': ['c#', 'powershell'],
	'amado': ['powershell', 'ruby'],
	'rio': ['go', 'haskell'],
}

print("\nLet's talk about favorite programming/scripting languages!\n")

for name, languages in favorite_languages.items():
	print(f"{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"{language.title()}")

#----------------------------------------------------------------Dictionary in a Dictionary-----------------------------------------------------------------
#Dictionaries can be nested within dictionaries. This can be useful in scenarios where we have similar dictionaries that can be stored under one title.
print("\n\nLet's make a users dictionary with a users and details!")

users = {
	'gocasio': {
		'first': 'giovanni',
		'last': 'ocasio',
		'location': 'new york',
	},
	'lcarreon': {
		'first': 'lisa',
		'last': 'carreon',
		'location': 'new jersey',
	},
	'rcarreon-ocasio': {
		'first': 'rio',
		'last': 'carreon-ocasio',
		'location': 'virginia',
	},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tResides In: {location.title()}")

#---------------------------------------------------------------------------Chapter Lab---------------------------------------------------------------------
print("\n\nPiecing it all together!")

cities = {
	'new york city': {
		'country': 'united states',
		'population': '8.2 million',
		'nickname': 'the big apple',
	},
	'london': {
		'country': 'great britain',
		'population': '8.8 million',
		'nickname': 'the square mile',
	},
	'paris': {
		'country': 'france',
		'population': '2.1 million',
		'nickname': 'the city of lights',
	},
}

for city, city_info in cities.items():
	city_name = f"{city}"
	country = f"{city_info['country']}"
	pop = city_info['population']
	nickname = f"{city_info['nickname']}"

	print(f"{city_name.title()} is located in {country.title()}. The population there is {pop} and it is known as {nickname.title()}!")
