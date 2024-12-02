#---------------------------------------------------------------------------Loops---------------------------------------------------------------------------
#In situations where we want to repeat the same action on every element of a list we'll use a 'for' loop
print("Let's print the name of every individual stored in the guests list!")
guests = ['john', 'leroy', 'diana', 'corinthia', 'emmanuel', 'vanessa', 'dave']

for guest in guests:
	print(guest)

#Python will associate the first item with the guest variable and prints the output. Since the list contains more values it returns to the first line of 
#the script and prints the next value. It will continue to do this until it has gone through each value in the list.
print("\n\nLet's have Python print a message for each guest")

for guest in guests:
	print(f"Thank you for the RSVP {guest.title()}!")

print("\n\nLet's add a second message.")

for guest in guests:
	print(f"Thank you for the RSVP, {guest.title()}!")
	print(f"{guest.title()}, we look forward to your participation!\n")

#Notice how both print commands are indented beneath the for loop. This means that both commands will be executed within the for loop. To execute a command
#outside the for loop we need to remove the indentation.
for guest in guests:
	print(f"I'm still talking to you, {guest.title()}!")
	print(f"{guest.title()}, we appreciate your participation!\n")

print("Now we're outside of the loop!")

#Indentation is very important in Python. A common error that comes up in Python is unintentional indentation or simply forgetting to indent. Unintentional
#indentation will result in commands listed after a for loop to be executed in conjuntion with the for loop. Forgetting to indent with result in a Python
#error or leaving a command that should run with the for loop out. Lastly, forgetting the colon ':' after the for loop will result in an error because
#Python does not understand what comes next.

#----------------------------------------------------------------------Numerical Lists----------------------------------------------------------------------
#Using the range() function to print numerical values.
print("\n\nLet's print a list of 1-20")

for value in range(1, 20):
	print(value)

print("Notice that the print command only printed 1-19. This is normal behavior in Python, it'll stop once it reaches the max value.")

#Storing the numerical values to a list.
print("\n\nWe can store the values to a list using the list() function.")

numbers = list(range(1, 21))
print(numbers)

#Skipping values with range
print("\n\nWe can also skipp values with the range() function!")
print(numbers)

even_numbers = list(range(2, 21, 2))
print(even_numbers)

print("\nThe range function will starts at 2, since that is what we specified, and will add 2 to this value until it reaches the max value of 21.")

print("\nWe can also perform other mathematical equations in conjuntion with our range valued list.")
squares = []
print("Our squares list is empty:", squares)
print("\nNow let's add the squared values of 1-15.")

for value in range(1, 16):
	squares.append(value**2)

print("Now we have a list of squared values:", squares)

#----------------------------------------------------------------------Simple Statistics---------------------------------------------------------------------
#We can also find the maximum value, minimum value, and sum of the numerical values in a list
print("\n\nThe minimum value of our squares list is:", min(squares))
print("The max value of our squares list is:", max(squares))
print("And the sum of our squares list is:", sum(squares))

#------------------------------------------------------------------------Slicing a List-----------------------------------------------------------------------
print("\n\nLet's use parts of a list!")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("This is our list:", players, "Let's select the index values of 2-5!")
print(players[2:5])

print("\nIf we omit the first index value it'll start with the first element in the list. Ex: print(players[:4])")
print(players[:4])

print("\nIf we omit the last index value it'll start with the specified firsst element in the list and continue until the last. Ex: print(players[3:])")
print(players[3:])

print("\nIf we want to output the last 3 values we can use -3:. Ex: print(players[-3:]). Let's add a few more values and see what the last 4 values are.")
players.append('randy')
players.append('joseph')
players.append('kayla')
print("This is our new list:", players)
print("These are the values if we use -4:", players[-4:])

#----------------------------------------------------------------------Looping a Slice List-------------------------------------------------------------------
#We can also use for loops in conjuntion with our slice list.
print("\n\nLet's congratulate our first 3 players")

for player in players[:3]:
	print(f"Congratulations: {player.title()}")

#----------------------------------------------------------------------Looping a Slice List-------------------------------------------------------------------
#In scenarios where we have a new list and need to incorporate values from an old list we can copy the values
print("\n\nLet's copy our players list to our new all_stars list!")

all_stars = []
print("This is our current all stars list:", all_stars)

print("Let's copy the values of our players list to our all stars list")
all_stars = players[:]

print("This is our new all stars list:", all_stars)

#-----------------------------------------------------------------------------Tuples--------------------------------------------------------------------------
#Python refers to values that cannot change as immutable. Immutable lists are called Tuples, tuples look just like a list except they use ().
print("\n\nLet's create a tuple!")

dimensions = (200, 50)

for dimension in dimensions:	
	print(dimension)

print("The only way to overwrite a tuple is by redefining the value. For example, this is the current value for the dimensions tuple:", dimensions)

dimensions = (450, 275)
print("This is my new value for the dimensions tuple:", dimensions)


