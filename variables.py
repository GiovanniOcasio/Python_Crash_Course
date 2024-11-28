#-------------------------------------------------------------------------Variables-------------------------------------------------------------------------
#Variables in Python labels data under a specified name that can be called for later on in the script:
#The message variable below stores the the Hello World 
message = "Hello World"

#Now we can print the string using the message variable:
print(message)

welcome = "Welcome to the Python Crash Course from No Starch Press"
print(welcome)

#Variables names can only contain letters, numbers, and underscores:
message2 = "See this is valid"
print(message2)

welcome_2 = "This is also okay"
print(welcome_2) 

#--------------------------------------------------------------------Variables & Method---------------------------------------------------------------------
#Python can also change the casing of a string using .title(), .upper(), .lower() in conjunction with the variable name:
example = "this is originally stored in all lowercaes"
print("This is the original string:", example)
print("Now we're using the title method", example.title()) 

example_2 = "tHiS iS sToReD iN rAnDoM cAsInG"
print("This is the original string:", example_2)
print("Now we're using the upper method:", example_2.upper())
print("Now we're using the lower method:", example_2.lower())

#--------------------------------------------------------------------Combining Variables---------------------------------------------------------------------
#Now we can also combine two variables into one variable combining the strings
f_name = "Giovanni"
l_name = "Ocasio"
full_name = f"{f_name} {l_name}"
print(full_name)

#Notice the single f before the called variables. This is required for Python to actually replace the variable names with the actual content of the variables.
#This is what happens if you run it without the f
f_name = "Giovanni"
l_name = "Ocasio"
full_name = "{f_name} {l_name}"
print(full_name)

#We can also use the f-strings to create a complete message and in conjuntion with methods
f_name = "giovanni"
l_name = "ocasio"
full_name = f"{f_name} {l_name}"
print("This is the original output:", full_name)
print("This is the output with the f-string:", f"Hello, {full_name.title()}!")
#In message3 we use the plus (+) sign to concatenate the strings together. This requires an additional space of the strings will be appended without the space
message3 = "We can also store it to a variable:" + " This is the output with the f-string: " + f"Hello, {full_name.title()}!" 
print(message3)

#---------------------------------------------------------------------Adding Whitespace----------------------------------------------------------------------
#Whitespace refers to nonprinting characters such as spaces, tabs, and end-of-line symbols
#In the instance below we are going to use the \t to add a tab space to the text
print("Without tab space")
print("\tWith tab space")

#We can also use the \n to move the text immediately after to a newline
print("Each should be on separate line: " + "Line One Line Two Line Three")
print("Now each are on separate lines, because I used the newline charater combination: " + "\nLine One \nLine Two \nLine Three")

#Lastly we can combine the \n\t to tab text on a newline
print("Let's combine the two: \n\t1: Hacking \n\t2: Cyber Security \n\t3: Developer")

#----------------------------------------------------------------------Avoiding Errors-----------------------------------------------------------------------
#Common syntax errors occur when using " and '. For example, a string using single quotes cannot have an apostrophy, so it is common practice to use double 
#quotes.
#View this example:
apostrophy = "Using Double Quotes, so I can include an apostrophy. Let's test it out"
print(apostrophy)