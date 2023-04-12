'''
Lab Chapter 5: If Statements
Date: 01/22/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Conditional statments
    2. if statements
    3. Using if statements with lists
'''
# 3
'''
alien_color = "green" # simple if statement
if alien_color.lower() == "green":
    print("The player just earned 5 points")
'''

#4
'''
alien_color = "yellow" # simple if else statement
if alien_color.lower() == "green":
    print("The player just earned 5 points")
else:
    print("The player just earned 10 points")
'''

#5
'''
colors = ['green', 'yellow', 'red'] # simple if elif else statement
for col in colors:
    if col == "green":
        print("The player just earned 5 points")
    elif col == "yellow":
        print("The player just earned 10 points")
    else:
        print("The player just earned 15 points")
'''
#7
'''
fave_fruits = ['banana', 'grapes', 'lemon', 'mango', 'santol']
allowed_fruits = ['melon', 'guava', 'santol', 'papaya', 'banana', 'mango', 'chico']

for fruit in fave_fruits:
    if fruit in allowed_fruits:
        print(f"Congratulations! You can enjoy {fruit} here since it is allowed to enter our beloved country")
    else:
        print(f"Sorry, but {fruit} is forbidden in our beloved country")
'''

#8
