#----------------------------------------------------------------------------User Input---------------------------------------------------------------------
#Majority of applications require the acceptance of user input. We can accept user input by using the input() method in Python.
print("Let's use the input() method to accept user input!")

name = input("\nSo let's start with your name: ")

print(f"\nHello, {name}!")

#We can also write prompts that are longer than one lime using a variable to store the prompt and using +=
prompt = f"It's really nice to meet you {name}!"
prompt += "\nHow old are you? "

age = input(prompt)
#So here we took the age of the user. The input() only accepts strings and will interpret the age variable as a string. We can resolve this with the int()
#method.
age = int(age)

print(f"\nSo, your name is {name} and you are {age} years old")

prompt_2 = f"\nWow, I can't believe you are {age} years old!"
prompt_2 += "\nIf you don't mind me asking. How are you feeling today? Good or Bad? "

mood = input(prompt_2)

if mood == 'Good':
	print("\nThat's great!")
else:
	print("\nI'm sorry to hear that.")

if age >= 21:
	prompt_3 = "Do you want to go to the bar? Yes or No? "
	choice = input(prompt_3)
	if choice == "Yes":
		print("Cool, let's go")
	else:
		print("Ok, want to do something else?")
elif age <= 21:
	prompt_4 = f"\nSince you are {age}, we can't go to the bar."
	prompt_4 += "\nWant to hang out somewhere else? Yes or No? "
	choice_2 = input(prompt_4)
	if choice_2 == "Yes":
		print("Cool, where do you want to go?")
	else:
		print("Oh, well that's too bad.") 

#--------------------------------------------------------------------------Modulo Operator------------------------------------------------------------------
#Modulo operator, divides one number by another number and give the remainder.
#Modulo operator, divides one number by another number and give the remainder.
print("\n\nLet's create a tool that determine if a number is even or odd!")

print("\nEnter a number, and I'll tell you if it is even or odd!")
number = input("Pick a number: ")

number = int(number)

if number % 2 == 0:
	print("The number is even!")
else:
	print("The number is odd!")

#------------------------------------------------------------------------Car Rental Project-----------------------------------------------------------------
print("\n\nLet's set up a car rental interaction!\n")


prompt = "Good evening, welcome to Ocasio's car rentals!"
prompt += "\nWhat is your name? "

customer = input(prompt)

prompt2 = f"\nHey {customer.title()}, the cars we have on the lot are a Subaru Impreza, Chevy Malibu, and a Honda Accord."
prompt2 += "Would any of these interest you? Yes or No? "

decision1 = input(prompt2)

if decision1 == 'Yes':
	prompt3 = "\nPerfect, which will it be? The Subaru, Chevy, or Honda? "
	choice = input(prompt3)
else:
	print("\nSorry that we can't be more helpful.")

if choice == 'Subaru':
	print(f"\nAwesome, let's get you that {choice}")

if choice == 'Chevy':
	print(f"\nAwesome, let's get you that {choice}")

if choice == 'Honda':
	print(f"\nAwesome, let's get you that {choice}")

#----------------------------------------------------------------------------While Loops--------------------------------------------------------------------
#for loops takes a colletion of items and runs a block of code on each item. On the other hand while loop run as long as a certain condition is true
print("\n\nLet run a while loop that'll continue until the current number value is not less than or equal to 5\n")

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

print("\n\nLet's make another while loop!")

prompt = "\nTell me something and I will repeat it back to you!"
prompt += "\nI will continue to repeat it until you tell me to 'Quit It!' "

message = ""

while message != 'Quit It!':
	message = input(prompt)

	if message != 'Quit It!':
		print(message)

print("\n\nAnother method of writing this prompt is by using a flag.")

#For a program that should run only as long as many conditions are true you should define one variable that determines whether or not the entire
#program is active

prompt2 = "\nCount to 10."
prompt2 += "\nOnce you reach 10 the application will end. "

active = True
count = ""

while active:
	count = int(input(prompt2))

	if count == 10:
		active = False
		print("Thanks for counting. Bye!")
	else:
		print("Keep Counting")

print("\n\nLet's use break to end a program early!")

prompt3 = "\nWhat cities have you visited?"
prompt3 += "\n(Enter 'end' when you want to finish) "

while True:
	city = input(prompt3)

	if city == 'end':
		break
	else:
		print(f"I'd love to go to {city.title()}")


#We can use the continue statement to return to the beginning of the loop. For example, below the code will add 1 to the current number.
#If the current number is divisible by 2, continue will tell Python to ignore the rest of the code and return to the beginning.

current = 0

print(f"\n\nThe current number is {current}")

while current < 10:
	current += 1
	if current % 2 ==0:
		continue

	print(current)


#Programmers should be careful to avoid infinite loops by ensuring that the conditions of a while loop can be met at some point within the loop.

#-----------------------------------------------------------------While Loops and Lists/Dictionaries--------------------------------------------------------
print("\n\nLet's make a while loop that will loop through a list of guest who haven't confirmed their attendance to an event.")

no_rsvp = ['lisa', 'rio', 'mateo', 'amado']
rsvp = []

while no_rsvp:
	pending_rsvp = no_rsvp.pop()

	print(f"Requesting response: {pending_rsvp.title()}")
	rsvp.append(pending_rsvp)

	print("We've received a response from:")
	for rsvp in rsvp:
		print(rsvp.title())

no_rsvp = ['lisa', 'rio', 'mateo', 'amado']
rsvps = []

while no_rsvp:
	pending_rsvp = no_rsvp.pop()

	print(f"Requesting response: {pending_rsvp.title()}")
	rsvps.append(pending_rsvp)

print("We've received a response from:")
for rsvp in rsvps:
		print(rsvp.title())

print("\n\nNow le't use the while loop to remove every instances of a specified number in a list.")

numbers = [11, 74, 92, 11, 75, 34, 98, 65, 11, 84, 93, 61, 50, 11, 46, 72, 69, 27, 82, 11, 65]

prompt = f"Here's our list of numbers {numbers}."
prompt += "\nNow let's remove every instance of the value of 11"

print(prompt)
print(f"\nThe current length of the list is {len(numbers)}\n")

while 11 in numbers:
	numbers.remove(int(11))

print(numbers)
print(f"The new length of the list is {len(numbers)}")

print("\n\nNow let's use a while loop to add users and their favorite food to a dictionary until we don't want anymore input\n")

responses = {}

polling_active = True

while polling_active:
	name = input("What is your name? ")
	food = input("What is your favorite food? ")

	responses[name] = food

	repeat = input("Would like to allow another vote? (Yes / No) ")
	if repeat == 'no':
		polling_active = False

print("-----Polling Complete-----")
for name, food in responses.items():
	print(f"{name.title()}'s favorite food is {food.title()}")


#----------------------------------------------------------------------------Chapter Lab--------------------------------------------------------------------
responses = {}

polling_active = True

while polling_active:
	name = input("What is your name? ")
	vacay = input("What is your dream vacation area? ")

	responses[name] = vacay

	repeat = input("Would like to allow another vote? (Yes / No) ")
	if repeat == 'no':
		polling_active = False

print("-----Polling Complete-----")
for name, vacay in responses.items():
	print(f"{name.title()}'s dream vacation area is {vacay.title()}")

input("Press Enter to exit... ")
