'''
Lecture Chapter 4: Working with Lists
Date: 01/20/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Looping through an entire list
    2. Making numerical lists
    3. Working with part of a list
    4. Tuples
'''
# Looping through an entire list
'''
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
repeat = 0

for tool in tools: # assigning each element of the list to the variable 'tool'
    print(tool.title())

for i in range(len(tools)): # using the range function and length of the list to access the elements of the list via its indices
    print(tools[i].title())
    repeat+=1

print(f"In total, the list contains {repeat} tools")
'''

# Making numerical lists
'''
for value in range(1, 6): # using the range function
    print(value)

numbers = list(range(1, 6)) # making a list of numbers using range function
print(numbers)

squares = []

for numbers in range(1, 11):
    squares.append(numbers ** 2) # performing operations prior to making elements of a list
print(squares)

squares = [value ** 2 for value in range(1, 12)] # basic list compression
print(squares)

tools = ['dewalt', 'bosch', 'makita', 'stanley', 'milwaukee','black & decker']
fave = tools[0:5] # basic slicing of a list (acccesing certain section of the list)
print(fave)

data = [0,  25, 12, 78, 13, 45, 68, 91, 72, 17]
order = sorted(data)
print(order) # sorting of numerical elements in a list in increasing order
data.sort()
print(data)
'''
# Tuples






