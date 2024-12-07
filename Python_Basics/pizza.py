def greetings(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

active = True
while active:
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")

    # Check if the first name is not empty and stop the loop if true
    if f_name != '':
        active = False

    # Only print the greeting if the first name is not empty
    formatted_name = greetings(f_name, l_name)
    print(f"Welcome, {formatted_name}! Let's get your order!")

def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")


