#----------------------------------------------------------------------------Functions----------------------------------------------------------------------
#Functions are lines of code designed to perform one task.
print("Let's create a function that greets users!\n")

def greet_user():
	"""Display a simple greeting"""
	print("Hello!")

greet_user()

print("We can also pass information the a function and when we call the function it will require input to execute.\n")

def greet_user(username):
	"""Display a simple greeting"""
	print(f"Hello, {username.title()}!")

greet_user('gina')

#The username variable in this scenario is a parameter, or a piece of information that is required for the function to execute. The value 'gina' is an
#argument, or a piece of information that is passed from a function call to a function.

def display_message():
	print("\nWe are learning about defining and calling functions in different scenarios!")

display_message()

def favorite_book(title):
	print(f"\nMy favorite book is {title.title()}")

favorite_book('harry potter and the half-blood prince')

#Sometimes a function may require multiple parameters and multiple arguments. In situations like this the position of the argument must correlate to 
#the position of the parameter. These are known as positional arguments.

#---------------------------------------------------------------------Positional Arguments------------------------------------------------------------------
print("\n\nLet's use positional arguments!\n")

def describe_pets(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pets('pig', 'peter porker')

print("\nWe can even call the same function multiple times with different arguments!\n")

describe_pets('spider', 'man-spider')
describe_pets('snake', 'basilisk')

print("\nLike the name entails the position of the argument matters in positional arguments.")

print("\nWe can also set default values for parameters in a function! Here we'll set animal_type=dog when we define the function.\n")

def dog_names(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

dog_names(pet_name='krypto')

prompt = "\nDespite there being a default argument value position still matters. We must place the default parameter last so it doesn't"
prompt += " interfere with the parameter we are going to pass later."

print(prompt)

#-------------------------------------------------------------------Returning Simple Values-----------------------------------------------------------------
print("\nWe can also have the use the function to return simple values.\n")

def musician_name(first_name, last_name):
	"""Return a full_name"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = musician_name('jimi', 'hendrix')
print(musician)

#----------------------------------------------------------------------Optional Arguments-------------------------------------------------------------------
print("\n\nWe can also make arguments optional!\n")

def musician_name(first_name, last_name, middle_name=''):
	"""Return a full_name"""
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = musician_name('jimi', 'hendrix')
print(musician)

musician = musician_name('john', 'hooker', 'lee')
print(musician)

#--------------------------------------------------------------------Returning Dictionaries-----------------------------------------------------------------
print("\n\nLet's define a dictionary within a fucntion and return the value!\n")

def build_person(first_name, last_name, middle_name=None):
	"""Return a dictionary of information about a person"""
	person = {'first': first_name, 'last': last_name}
	if person:
		person['middle_name'] = middle_name
	return person

hacker = build_person('elliot', 'alderson', middle_name ='mr. robot') 
print(hacker)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------While Loops w/ Funtions-----------------------------------------------------------------
print("\n\nLet's use a while loop with our fucntion and return the value!\n")

def musician_name(first_name, last_name, middle_name=''):
	"""Return a full_name"""
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name.")
	print("Type 'q' to quit.")
	f_name = input("First Name: ")
	if f_name == 'q':
		break
	l_name = input("Last Name: ")
	if l_name == 'q':
		break

	musician = musician_name(f_name, l_name)
	print(f"\nHello, {musician}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def places_to_visit(visit_city, visit_country):
	place = f"{visit_city}, {visit_country}"
	return place.title()

while True:
	print("\nPlease tell me what city and country you want to visit.")
	print("Type 'q' to quit.")
	city = input("City: ")
	if city == 'q':
		break
	country = input("Country: ")
	if country == 'q':
		break

	where_to_go = places_to_visit(city, country)
	print(f"\nHello, {where_to_go}")

#----------------------------------------------------------------------Passing a List------------------------------------------------------------------------
print("\n\nWe can incorporate lists with out functions!\n")

def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['hannah', 'tom', 'margot', 'tommy', 'james', 'tasha', 'angela']
greet_users(usernames)

#----------------------------------------------------------------------Modifying List------------------------------------------------------------------------
print("\n\nLet's create a function that uses a list and modifies the list!\n")

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print(f"\nThe following models have been printed: ")
	for models in completed_models:
		print(completed_models)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


