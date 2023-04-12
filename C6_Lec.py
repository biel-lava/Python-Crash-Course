'''
Lecture Chapter 6: Dictionaries
Date: 01/23/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Working with dictionaries
    2. Looping through a dictionary
    3. Nesting
'''
# Working with dictionaries
'''
simple_dict = {'name': 'elsa'} # simplest dictionary and accessing the value using the key
print(simple_dict['name'].title())

simple_dict = {'name':'elsa'} # assigning a new key-value pair in an existing dictionary
simple_dict['title'] = 'queen'
simple_dict['location'] = 'arendelle'
print(simple_dict)

simple_dict = {'name':'elsa'} # modifying a value associated with a specific key
print(simple_dict)
simple_dict['name'] = 'anna'
print(simple_dict)

simple_dict ={'queen':'elsa', 'princes':'anna', 'minister':'olaf'} # deleting a key value pair using the del function
print(simple_dict)
del simple_dict['minister']
print(simple_dict)

simple_dict ={'queen':'elsa', 'princes':'anna', 'minister':'olaf'} # using the get method to know whether or not a certain key exists in a dictionary
my_role = simple_dict.get('king', 'You do not exist to the specified universe')
print(my_role)
'''

# Looping through a dictionary
'''
fave_cars = { # a different way to write a dictionary (mas malinis tingnan)
    'oyie':'bus',
    'philip':'wigo',
    'allen':'gravis',
    'renz':'cargo ship',
    'biel':'pick up' 
}
for names, cars in fave_cars.items(): # using a for loop and the "items" method to access every key-value pair in a dictionary
    print(f"For {names.title()}, his favorite car is a {cars.title()}")

fave_cars = { # a different way to write a dictionary (mas malinis tingnan)
    'oyie':'bus',
    'philip':'wigo',
    'allen':'gravis',
    'renz':'cargo ship',
    'biel':'pick up' 
}
for names in fave_cars.keys(): # using the "keys" method to only work with either the key or the values of the dictionary
    print(f"Hello {names.title()}!")

fave_cars = { # a different way to write a dictionary (mas malinis tingnan)
    'oyie':'bus',
    'philip':'wigo',
    'allen':'gravis',
    'renz':'cargo ship',
    'biel':'pick up' 
}

for cars in fave_cars.values():
    print(cars.title()) # using the "values" method to access only the values of a certain dictionary
'''

# Nesting (list of dictionaries)
'''
oyie = {'course':'civil eng', 'car':'bus'}
philip = {'course':'mech eng', 'car':'wigo'}
allen = {'course':'physical therapy', 'car':'gravis'}

friends = [oyie, philip, allen] # simple list of dictionaries
for frends in friends:
    print(frends)

troops = []
for troop in range(30): # using a for loop to create a list of dictionaries
    new_soldier = {'uniform':'blue', 'weapon':'M4A1', 'unit':'infantry'}
    troops.append(new_soldier)
for soldiers in troops[0:15]: # changing the value of certain elements in the dictionary
    if soldiers['uniform'] == 'blue':
        soldiers['uniform'] = 'yellow'
        soldiers['weapon'] = 'NLAW'
        soldiers['unit'] = 'anti-tank'
for men in troops:
    print(men)
'''

# Nesting (dictionary of lists)
pizza = {
    'crust':'thick',
    'toppings': ['cheese', 'olives', 'beef', 'mushroom', 'peperoni'] # having the value associated to a certain key a list
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:") # accessing the list contained in a dictionary
for toppings in pizza['toppings']:
    print("\t" + toppings)












