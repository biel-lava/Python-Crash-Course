'''
Chapter 2: Variables and Simple Data Types
Date: 01/17/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Strings
    2. Numbers
'''

#Strings Lecture Section
'''
name = input("What is your name: ")
proper_name = name.title() #title function
print(proper_name)
'''
'''
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = f"{first_name} {last_name}" #f-string
statement = f"Hello, {full_name.title()}!"
print(statement)
'''

#Strings Exercises Section
#1
'''
name = input("What is your name? :")
greet = "would you like to learn some Python today?"
message = f"Hello, {name.title()} {greet}"
print(message)
'''

#2
'''
name = input("Insert name: ")
upper = name.upper()
lower = name.lower()
proper = name.title()
print(f"{name} \n{upper} \n{lower} \n{proper} ")
'''

#3
'''
quote = 'Marcus Aurelius once said, "Do not think what is hard for you to master is humanly impossible \nand if it is humanly possible, consider it within your reach"'
print(quote)
'''

#5


