#---------------------------------------------------------------------------List----------------------------------------------------------------------------
#A list is a collection of items in a particular order. In Python, square brackets indicate a list and individual elements are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("This is an example of a list:", bicycles)

#We can specify which element we want to print by telling Python the index or position of the element. Note, the first element in a list in Python is 
#identified as 0
print("This is the first item in the list:", bicycles[0])

#We can also use string methods to format the elements we select
print("Now we'll use the title method:", bicycles[0].title())
print("Now we'll use the upper method:", bicycles[0].upper())

#As stated previously the first element in a Python list is identified by the position value of zero (0). But the last element can be identified by the value
#of -1
print("Now let's print the last item:", bicycles[-1])

#We can aslso use the f-strings to create a message based on the value of a list
message = f"My first bicycle was a {bicycles[-1].title()}"
print(message)

#----------------------------------------------------------------Modifying Elements of a List-----------------------------------------------------------------
#We can also modify the elements of a list by specifying the list, the element's index value we want to change, and what we want to change it to. 
print("\n\nLet's modify our list!")

motorcycles = ['honda', 'yamaha', 'suzuki']
print("This is our current list:", motorcycles)

motorcycles[0] = 'ducati'
print("Now let's change honda to ducati", motorcycles)

#------------------------------------------------------------------Adding Elements of a List------------------------------------------------------------------
#We can also add elements to a list by using append. Appending adds items to the end of a list without affecting other elements.
print("\n\nLet's add elements to our list!")

print("This is our current list:", motorcycles)
motorcycles.append('honda')
print("Now let's append honda to our new list:", motorcycles)

#----------------------------------------------------------------Inserting Elements of a List-----------------------------------------------------------------
#We can also insert elements into specified positions by using insert.
print("\n\nLet's insert elements into our list")

print("This is our current list:", motorcycles)
print("Let's insert harley davidson into the list at index 3")
motorcycles.insert(3, 'harley davidson')
print(motorcycles)

#-----------------------------------------------------------------Deleting Elements of a List-----------------------------------------------------------------
#We can remove elements from a list by using del.
print("\n\nLet's delete elements from our list!")

print("This is our current list:", motorcycles)
del motorcycles[3]
print("We removed harley davidson", motorcycles)

#------------------------------------------------------------------Popping Elements of a List-----------------------------------------------------------------
#Using pop we can remove an element and store it for later use. In this scenario we'll store the popped item to another variable and call it later.
print("\n\nLet's pop elements to our list!")

motorcycles.append('harley davidson')
print("This is our current list:", motorcycles)

popped_item = motorcycles.pop()
print("We popped the last brand:", motorcycles)
print("What we popped was", popped_item)

#We can also use index values to specify the element we want to pop.
motorcycles.append('harley davidson')
print(motorcycles)

popped_item = motorcycles.pop(2)
print("We popped the element with the index value of 2", motorcycles)
print("We popped", popped_item)

#-----------------------------------------------------------------Removing Elements of a List-----------------------------------------------------------------
#If you don't know the index value of an element but you know the actual value you can remove that value
print("\n\nLet's remove elements from our list!")

print("This is our current list:", motorcycles)
print("Let's use remove to take out yamaha.")
motorcycles.remove('yamaha')
print("We removed yamaha so now our list contains:",motorcycles)

#Let's create a variable to store our favorite bike. Then use the variable to remove it from the list

favorite_bike = 'ducati'
motorcycles.remove(favorite_bike)
print(motorcycles)

#Let's use f-string and new line to specify which element we removed
print(f"\nA {favorite_bike} is my favorite motorcycle to ride!")

#-----------------------------------------------------------------------Organizing List-----------------------------------------------------------------------
#We can organize list in different ways
print("\n\nWe can permanently sort a list using the sort() method")
cars = ['honda', 'bmw', 'subaru', 'audi']
print("This is the original list", cars)
cars.sort()
print("Now sort() will permanently alphabetizes the list:", cars)

#Temporarily sorted list

print("\n\nWe can temporarily sort list using the sorted() method. We will input the list name into the sorted() parenthesis.")
cars_2 = ['toyota', 'camry', 'chevy', 'benz']
print("This is the original list:", cars_2)
print("This is the temporarily sorted list:", sorted(cars_2))
print("All we have to do is remove sorted() and our list will return to its original format:", cars_2)

#Sorting list in reverse order
print("\n\nWe can also print list in reverse order using the reverse() method")
print("Here's the original format", cars_2)
cars_2.reverse()
print("This is the list in reverse order", cars_2)

#----------------------------------------------------------------------Lengtt of a List-----------------------------------------------------------------------
#We can determine the length of a list by using the len() method
print("\n\nLet's use the len() method to determine the length of a list")
vehicles = ['toyota', 'camry', 'chevy', 'benz', 'honda', 'bmw', 'subaru', 'audi', 'ducati', 'yamaha', 'harley davidson']
print("This is our list:", vehicles)
print(len(vehicles))
