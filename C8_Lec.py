'''
Lecture Chapter 8: Functions
Date: 01/25/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Defining a function
    2. Passing arguments
    3. Return values
    4. Passing a list
    5. Passing an arbitrary number of arguments
    6. Storing functions in modules
'''

# Defining a function
'''
def morning_greeting(): # simplest form of a function
    print("Good morning Elsa!")

morning_greeting()
'''

# Passing arguments
'''
def pets(name, pet): # using multiple parameters sa function definition
    print(f"\nMy name is {name.title()}")
    print(f"I have a pet {pet}")

pets('biel','cat') # using multiple positional arguments (mahalaga yung order ng arguments sa function call) in the function call

def home(name, home = 'the Philippines'): # using a default value for a parameter for cases na walang argument dun sa function call
    print(f"Hello! My name is {name.title()} and I live in {home}")

home("biel", "rizal") # since an argument is the parameter home is given, ignored na yung default value na nakalagay sa function definition
home("elsa")
'''

# Passing a List
'''
friends = ['allen', 'oyie', 'philip', 'renz', 'eca']

def greetings(names): # passing a list into a function
    for name in names:
        print(f"Hello, {name.title()}!")

greetings(friends)

pending_orders = ['cordless drill', '4 inch grinder', 'table saw', 'router', 'shop vac', 'dremel']
completed_orders = []

def process(pending, complete): # using a function to modify a list
    while pending:
        current_order = pending.pop()
        print(f"Currently processing: {current_order.title()}")
        complete.append(current_order)
    show_order(complete)

def show_order(completed):
    print("Orders complete! Here is the summary of your order: ")
    for orders in completed:
        print(f"\t{orders.title()}")

process(pending_orders, completed_orders)
'''

# Passing an arbitrary number of arguments
'''
def toppings(*tops): # * is used for instances where indefinite yung amount ng arguments passed sa function call
    for contents in tops: # the arguments from the function call are stored in a tuple (immutable list)
        print(contents.title())

toppings('tomato', 'cheese', 'mushroom', 'olives', 'sausage')
'''

# Storing functions in modules
'''
import practice_module # Most basic example of importing another module (another python file with specific functions)

tropa = ['allen', 'oyie', 'philip', 'renz', 'eca']
practice_module.print_friends(tropa)

from practice_module import print_friends, greetings # importing specific functions from a module
tropa = ['allen', 'oyie', 'philip', 'renz', 'eca']
print_friends(tropa)
greetings(tropa)
'''
from practice_module import print_friends as pf, greetings as g # using alias to represent imported functions

tropa = ['allen', 'oyie', 'philip', 'renz', 'eca']

pf(tropa)
g(tropa)












