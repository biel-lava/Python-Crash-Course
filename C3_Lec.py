'''
Lecture Chapter 3: Introducing Lists
Date: 01/17/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Accessing list elements
    2. Modifying list elements
    3. Adding list elements
    4. Removing list elements
'''

#Accessing list elements
'''
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
print(tools[5].title())
'''

#Modiying elements to the list
'''
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
tools[4] = 'TEH' # assigning new element to the list
print(tools)
'''

#Adding elements to a list (append and insert)
'''
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
tools.append('hitachi') # adds new element to the last of the list
tools.insert(2, 'dewalt') # adds a new element to a specific location in the list
print(tools)
'''

#Removing elements from a list (pop, delete and remove)
'''
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
del tools[2] # deletes a certain element of the list permanently based on its index
print(tools)
first_tool = tools.pop() # removes the last item from the list (since walang ginamit na index) and assigns it into a new variable
print(first_tool)
fave_tool = tools.pop(0) # pops a certain element of the list based on its index and assigns it into a new variable
print(f"My favorite brand of powertools is {fave_tool.title()}")
tools.remove('stanley') # removes a certain element if we know the value of that element
print(tools)
'''

# Organizing a list (sort, sorted, reverse, len)
tools = ['dewalt', 'milwaukee', 'makita', 'stanley', 'bosch','black & decker']
#tools.sort() # method that permanently sorts the list alphabeticaly
#tools.sort(reverse=True) # permanently sorts the list alphabeticaly but in reverse order(via the reverse=true argument)
products = sorted(tools) # function that temporarily sorts the list without affectinf the original list (reverse=true argument could also be used)
print(tools)
print(products)







