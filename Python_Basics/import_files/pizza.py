def greetings(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
