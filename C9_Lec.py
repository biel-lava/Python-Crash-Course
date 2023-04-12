'''
Lecture Chapter 9: Classes
Date: 01/28/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Creating and using a class
    2. Working with classes and instanes
    3. Inheritance
    4. Importing classes
'''

# CREATING AND USING A CLASS #
'''
class Dog:
    def __init__(self, name, age): # ito yung constructor ng class
        # initialize the attributes name and age of the dog
        # every attribute with the prefix self is accessible to all of the instances of the class
        self.name = name # works by getting the value of the parameter name and passing it to the attribute name 
        self.age = age
        self.vaccines = 0 # setting an attribute with a default value (hindi kasama sa parameter ng constructor call)
        self.tricks = 0

    def sit(self): # basic methods for the class dog with only self as the parameter
        print(f"{self.name.title()} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name.title()} rolled over! ")

    def update_tricks(self, tricks): # a method that would update the value of an attribute (pinaka basic)
        self.tricks = tricks



# making an instance of the class Dog
my_dog = Dog("Landi", 4)

# accessing the different methods of the class
my_dog.roll_over()
my_dog.sit()

# accessing the different attributes of the class
print(my_dog.age)
print(my_dog.name)

# modifying the value of an attribute
my_dog.vaccines = 2 # directly
print(f"{my_dog.name.title()} has {my_dog.vaccines} vaccines already")

my_dog.update_tricks(5)
print(f"My dog {my_dog.name.title()} already knows {my_dog.tricks} tricks!")
'''

# INHERITANCE #

class Car: # this is the parent class
    def __init__(self, make, model, year): # constructor
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    # MODULES of the class Car
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
    
    def increment(self, miles):
        self.odometer_reading += miles
    

class ElectricCar(Car): # pinaka basicc example of a child class
    def __init__(self, make, model, year): # important to initialize the attributes of the parent class
        super().__init__(make, model, year) # the super function allows the child class to call a method from the parent class
        self.battery = 75 # making a subclass level attribute (para sa subclass lang)

tesla = ElectricCar('tesla', 'models s', 2019) # make a new instance of the subclass electic car

print(tesla.get_descriptive_name())
    