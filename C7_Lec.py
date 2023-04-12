'''
Lecture Chapter 7: User input and while loops
Date: 01/25/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. How the input function works
    2. Introducing while loops
    3. Using a while loop with lists and dictionaries
'''
# How the input function works
'''
statement = "If you tell us who you are, we can personalize the messages you see." 
statement += "\nWhat is your name?: " # How to make a prompt (yung statement na lumalabas before the input part) with multiple lines

name = input(statement)
print(f"Hello, {name.title()}!")

vhf_freq = 136.000
vhf = []
uhf_freq = 400.000
uhf = []
while vhf_freq <= 174.000: # using a while loop to make a list of certain numbers
    vhf.append(vhf)
    vhf_freq += 0.0025
while uhf_freq <= 520.000:
    uhf.append(uhf)
    uhf_freq += 0.0025
print(f"The number of possible VHF channels for Baofeng radios are {len(vhf)}")
print(f"The number of possible UHF channels for Baofeng radios are {len(uhf)}")

instructions = "\nThis monitor will display any message you want to tell the world."
instructions += "\n Just type 'quit' if you have nothing to say anymore."
instructions += "\n What do you want to say to the world?: "

status = True # using boolean as a flag for the conditions of the while loop

while status:
    message = input(instructions)
    if message != 'quit':
        print(message)
    else:
        status = False
'''

# Using while loop with Lists and Dictionaries
'''
unconfirmed_users = ['oyie', 'allen', 'philip', 'renz', 'eca']
confirmed_users = []

while unconfirmed_users: # condition for while loop remains True as long as the list is not empty
    current = unconfirmed_users.pop()
    print(f"Verifying user: {current.title()}")
    confirmed_users.append(current)
print("\nUser verification completed!")
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(f"User: {user.title()}")
'''

responses = {}
poll_active = True
print("Welcome to the Favorite Food Tracker for this year!")

while poll_active: # using a while loop to fill up a dictionary
    name = input("What is your name?: ")
    response = input("What is your favorite food?: ")

    responses[name] = response

    another_entry = input("Would you like to enter another person's food? Yes or No: ")
    if another_entry == "no":
        poll_active = False

print("\n---------POLL RESULTS---------")
for name, response in responses.items():
    print(f"For {name.title()}, the best food this year is {response}!")



