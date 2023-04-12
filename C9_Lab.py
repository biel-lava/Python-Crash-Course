'''
Lab Chapter 9: Classes
Date: 03/28/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Creating and using a class
    2. Working with classes and instanes
    3. Inheritance
'''

#1
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} which specializes in {self.cuisine.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open")


selinas = Restaurant("selinas", "filipino household")

selinas.describe_restaurant()
selinas.open_restaurant()
'''
#2
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe name of the restaurant is {self.name.title()} which specializes in {self.cuisine.title()} dishes")


    def open_restaurant(self):
        print(f"{self.name.title()} is now open")


selinas = Restaurant("selinas", "filipino household")
cadapans = Restaurant("cadapans", "chicken")
panda = Restaurant("dimsum panda", "fried dumpling")

selinas.describe_restaurant()
cadapans.describe_restaurant()
panda.describe_restaurant()
'''

#3
'''
class User:
    def __init__(self, first_name, last_name, batch, camera_brand):
        self.first = first_name
        self.surname = last_name
        self.batch = batch
        self.brand = camera_brand

    def describe_user(self):
        print(f"{self.first.title()} is from batch {self.batch.title()} and is loyal to {self.brand.title()}")


biel = User("biel", "lava", "RAW", "nikon")
biel.describe_user()

kyla = User("kyla", "patricia", "lomography", "nikon")
kyla.describe_user()

yohann = User("yohann", "cortez", "Kodak", "canon na panget")
yohann.describe_user()

shawie = User("shawie", "fabellar", "spectra", "astrid")
shawie.describe_user()
'''

#4
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type): #constructor 
        self.name = restaurant_name # attributes
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} which specializes in {self.cuisine.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open")

    def set_number_served(self, customer_count):
        print(f"The current number of customers served by {self.name.title()} is {self.number_served}")
        self.number_served = customer_count
        print(f"The updated current number of customers served by {self.name.title()} is {self.number_served}")


selinas = Restaurant("selinas", "filipino household")

selinas.describe_restaurant()
selinas.open_restaurant()

selinas.set_number_served(6)
'''

#5
'''
class User:
    def __init__(self, first_name, last_name, batch, camera_brand):
        self.first = first_name
        self.surname = last_name
        self.name = f"{self.first.title()} {self.surname.title()}"
        self.batch = batch
        self.brand = camera_brand
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first.title()} is from batch {self.batch.title()} and is loyal to {self.brand.title()}")

    def increment_login_attempts(self, new_login_count):
        print(f"Updating the login attempts of {self.name.title()} .....")
        self.login_attempts = new_login_count
        print(f"Login attempts updated successfully! Thw updated login attempts for {self.name.title()} is {self.login_attempts}")

    def reset_login_attempts(self):
        print(f"The current login attempts of {self.name.title()} is {self.login_attempts}")
        self.login_attempts = 0
        print("Reset completed for the number of login attempts")
        print(f"The updated number of login attempts for {self.name.title()} is {self.login_attempts}")

elsa = User("elsa", "lava", "raw", "nikon")
elsa.describe_user()
elsa.increment_login_attempts(9)
elsa.reset_login_attempts()
'''

#6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type): #constructor 
        self.name = restaurant_name # attributes
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} which specializes in {self.cuisine.title()} dishes")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open")

    def set_number_served(self, customer_count):
        print(f"The current number of customers served by {self.name.title()} is {self.number_served}")
        self.number_served = customer_count
        print(f"The updated current number of customers served by {self.name.title()} is {self.number_served}")

class IceCreamShop(Restaurant):
    def __init__(self, restaurant_name, cuisine_type): # initialization of the methods of the subclass attributes (inherrited from the superclass)
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "cookies and cream", "choco fudge"]

    def display_flavors(self):
        print("The available flavors: ")
        for i in range(len(self.flavors)):
            print(self.flavors[i])

dq = IceCreamShop("DQ", "classic ice creams")
dq.describe_restaurant()
dq.display_flavors()

#7









