'''
Lab Chapter 4: Working with Lists
Date: 01/21/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Accessing list elements
    2. Modifying list elements
    3. Adding list elements
    4. Removing list elements
'''
# 1
'''
fave_pizza = ['all cheese', 'beef sausage', 'pepperoni', 'margherita']
for pizza in fave_pizza: # based pn the assignment of the list 
    print(f"I really love {pizza.title()}")
for i in range(len(fave_pizza)): # based on elelement' index
    print(f"I really love {fave_pizza[i].title()}")
'''

#2
'''
claws = ['cat', 'tiger', 'lion']

for pets in claws:
    print(f"A {pets.title()} would make a great pet!")
print("Any of these animals would make a great pet!")
'''

#3
'''
for number in range(1,21):
    print(number) # printing a set of numbers using a for loop
'''

#5
'''
number = list(range(1, 1000001)) # using list function to make a list with numbers from 1 to 1 million
print(min(number))
print(max(number))
print(sum(number)) # getting the sum of the list of numbers from 1 to 1 million
'''

#6
'''
odds = list(range(1, 21, 2)) # making a list of odd numbers using the third argument of the range function
for num in odds:
    print(num)
'''

#7
'''
three = list(range(3, 31, 3)) # making a list of numbers divisible by three using the third argument of the range function
for num in three:
    print(num)
'''

#8
'''
cubes = [ values **3 for values in range(0, 11)] # using list compression to make a list of the cubes of the first 10 integers
for val in cubes:
    print(val)
'''

#10
'''
three = list(range(0, 31, 3)) # using slice to access certain elements of a list
print(f"The first three items of the list are {three[0:3]}")
mid_list = int((len(three))/2)
print(f"The three items at the middle of the list are {three[mid_list-1:mid_list+2]}")
print(f"The last three elements of the list are {three[-3:]}")
'''

#11
'''
fave_pizza = ['all cheese', 'beef sausage', 'pepperoni', 'margherita']
friends_pizza = fave_pizza[:] # making a new list by copying the elements of the original list
fave_pizza.append('all beef')
friends_pizza.append('all shrimp')
print("My friends' fave pizzas are:")
for friends in friends_pizza:
    print(friends)
print("My personal fave pizzas are:")
for me in fave_pizza:
    print(me)
'''

#13
basic_foods = ('ham', 'turkey', 'lasagna', 'carbonara', 'cake')
for fuds in basic_foods:
    print(fuds.title())
revised_foods = ('roasted chicken', 'relleno', 'baked mac', 'spaghetti', 'fruit salad')
print("Revised menu:")
for fods in revised_foods:
    print(fods.title())

