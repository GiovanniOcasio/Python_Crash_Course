#------------------------------------------------------------------------Reading From Files-----------------------------------------------------------------
#We can use Python to Read the content of files.
with open('python.txt')as file_object:
	contents = file_object.read()
print(contents)

#In Python read() returns the content with an additional black space. We can remove this extra space with rstrip.
with open('python.txt')as file_object:
	contents = file_object.read()
print(contents.rstrip())

#Python can dig down into directories where the script is located and can also use the absolute path to a file.
with open(r'C:\Windows\System32\drivers\etc\hosts') as file_object:
	contents = file_object.read()
print(contents.rstrip())

with open('folder\python.txt')as file_object:
	contents = file_object.read()
print(contents.rstrip())

#-------------------------------------------------------------------Reading Lines From Files----------------------------------------------------------------
filename = r"folder\multi.txt"

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


#--------------------------------------------------------------------Making Lists From Lines----------------------------------------------------------------
filename = r"folder\multi.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

#-------------------------------------------------------------------Working with File Content---------------------------------------------------------------
filename = r"folder\multi.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

content = ''
for line in lines:
	content += line.rstrip()

print(content)

filename = r"C:\Users\gocas\OneDrive\Documents\Python_Projects\folder\pi.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

#We can also view if portions of the strong matches user input
birthday = input("Enter your birthday, mmddyy:")
if birthday in pi_string:
	print("Your birthday can be found in Pi")
else:
	print("Your birthday was not found in Pi")

#------------------------------------------------------------------------Writing to Files-------------------------------------------------------------------
#We can also use Python to write to a file
filename = 'programming.txt'
#The 'w' specifies that we want to write to the file. 'r' specifies read-only, 'a' specifies append, and 'r+' specifies read and write.
#with open(filename, 'w') as file_object:
#	file_object.write("I love Programming")

#We can also write multiple lines
#with open(filename, 'w') as file_object:
#	file_object.write("I love Programming")
#	file_object.write("I love creating new games!")

#We can also append
with open(filename, 'w') as file_object:
	file_object.write("I love Programming\n")
	file_object.write("I love creating new games!\n")

with open(filename, 'a') as file_object:
	file_object.write("I also love using Python\n")
	file_object.write("Bash is pretty cool too!\n")

#-----------------------------------------------------------------------Handling Exceptions-----------------------------------------------------------------
#You can use a try-except block to handle exceptions that might come up.
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#We can incorporate this into a longer script and use it in conjunction with an else block.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit" )

while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond Number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

#We can also use this exception for FileNotFoundErrors

filename = 'I_do_not_exist.txt'
try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")

#We can also analyze the text using the split() method
filename = 'programming.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words")


#Much of this code can be added to a function and allows it to be called for multiple files
def count_words(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

filenames = ['programming.txt', 'python.txt']
for filename in filenames:
	count_words(filename)

#We can also use pass to have the script skip over the exception
def count_words(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

filenames = ['programming.txt', 'not_here.txt', 'python.txt']
for filename in filenames:
	count_words(filename)


#----------------------------------------------------------------------------Using Json---------------------------------------------------------------------
#We can use json.dump() and json.load() to store and reuse data.
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)

import json

#Load usernames that have been stored, if not stored prompt for username
filename = r'C:\Users\gocas\OneDrive\Documents\Python_Projects\usernames.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We'll remember you next time {username.title()}!")
else:
    print(f"Welcome back, {username.title()}")

input("Press Enter to Quit")

#---------------------------------------------------------------------------Refactoring---------------------------------------------------------------------
import json

def get_stored_username():
	filename = r'C:\Users\gocas\OneDrive\Documents\Python_Projects\usernames.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	username = input("What is your name?: ")
	filename = r'C:\Users\gocas\OneDrive\Documents\Python_Projects\usernames.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username 

def greet_user():
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username.title()}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username.title()}")

greet_user()
input("Is there anything else I can help you with?")


#---------------------------------------------------------------------------Chapter Lab---------------------------------------------------------------------
import json

def get_stored_username():
    filename = r'C:\Users\gocas\OneDrive\Documents\Python_Projects\usernames.json'
    try:
        with open(filename, 'r') as f:
            usernames = json.load(f)
            return usernames  # Return the list of usernames
    except (FileNotFoundError, json.JSONDecodeError):
        return None  # Return None if file is empty or corrupted

def get_new_username(user):
    filename = r'C:\Users\gocas\OneDrive\Documents\Python_Projects\usernames.json'
    
    # Try to load existing usernames from the file
    try:
        with open(filename, 'r') as f:
            usernames = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        usernames = []  # If the file doesn't exist or is empty, create a new list
    
    # Add the new user to the list if not already in it
    if user not in usernames:
        usernames.append(user)
    
    # Save the updated list of usernames back to the file
    with open(filename, 'w') as f:
        json.dump(usernames, f)
    
    return user  # Return the username

def greet_user():
    user = input("Please provide your name: ")
    usernames = get_stored_username()
    
    # If the username exists in the list, greet the user
    if usernames and user in usernames:
        print(f"Welcome back, {user.title()}!")
    else:
        user = get_new_username(user)
        print(f"We'll remember you when you come back, {user.title()}")

greet_user()
input("Is there anything else I can help you with?")
