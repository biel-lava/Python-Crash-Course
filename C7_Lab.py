'''
Lab Chapter 7: User input and while loops
Date: 01/25/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. How the input function works
    2. Introducing while loops
    3. Using a while loop with lists and dictionaries
'''
#1
'''
statement = "\nWelcome to Rent a Car!"
statement += "\nWhat car are you feeling to drive today?: "

car = input(statement)
print(f"Ah I see! Let me check if I can find you a {car.title()}")


#2
welcome = "\nWelcome to Alona's!"
welcome += "\nIlan po kayo na kakain tonight?: "

customers = int(input(welcome))

if customers >=8 :
    print("Sorry po! Mukhang need niyo po muna maghintay for a while since marami po ang kumakain sa Alona's! ")
else:
    print("This way to your seats po!")

#3
num = int(input("Enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")


#4
while True:
    print("\nWhat do you want to add to your pizza? If you have nothing more to add just type 'end'.")
    topping = input("Pizza topping to add: ")
    if topping == "end":
        break
    else:
        print(f"\nNoted! We will add {topping} to your pizza!")


#5
statement = "\nWelcome to the Broke Ass Ticket Calculator!"
statement += "\nTo exit the calculator just type 'end'."
statement += "\nPlease enter your age to check your ticket price: "

while True:
    age = int(input(statement))
    if age < 3:
        print("Congratulations! Your ticket is free.")
    elif age > 3 and age <= 12:
        print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15.")
    elif age == 'end':
        break


#8
sandwich_orders = ['clubhouse', 'chopped cheese', 'ham and cheese', 'grilled cheese']
finished_orders = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made you a {order.title()}")
    finished_orders.append(order)
print("The final list of sandwich orders:")
for orders in finished_orders:
    print(orders)
'''

#9
sandwich_orders = ['clubhouse', 'pastrami', 'chopped cheese', 'ham and cheese', 'pastrami', 'grilled cheese', 'pastrami']

print(sandwich_orders)

while 'pastrami' in sandwich_orders: # as long as may pastrami na element yung list, the while loop will continue
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

