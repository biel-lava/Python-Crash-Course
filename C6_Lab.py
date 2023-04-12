'''
Lecture Chapter 6: Dictionaries
Date: 01/24/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Working with dictionaries
    2. Looping through a dictionary
    3. Nesting
'''
# 1
'''
queen = {'first_name':'elsa', 'last_name':'lava', 'age':'31', 'city':'binangonan'}
for data in queen:
    print(queen[data].title())
'''

#2
'''
fave_num = {
    'oyie':'8',
    'allen':'9',
    'philip':'17',
    'renz':'21',
    'eca':'20'
}

for name,num in fave_num.items():
    print(f"For {name.title()} the best number is {num}")
'''

#3
'''
glossary = {
    'list':'a collection of items in a particular order',
    'index':'the position of a certain item in a list',
    'tuple':'an immutable list',
    'dictionary':'a collection of key-value pairs',
    'key':'an equivalent to the index in lists and is used to access the values in a dictionary'
}

for word, definition in glossary.items():
    print(f"\n{word.title()} is {definition}")
'''

#5
'''
rivers = {
    'nile':'egypt',
    'pasig':'pasig city',
    'yang tze': 'china'
}

for riv, nation in rivers.items():
    print(f"The {riv.title()} runs through {nation.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
'''

#6
'''
hooman = ['oyie', 'allen', 'renz', 'philip']
responses = {
    'john':'c',
    'renz':'python',
    'kyla':'ruby',
    'allen':'java',
    'philip':'java script'
}

for response in hooman:
    if response in responses.keys():
        print(f"Thank you for your entry {response.title()}")
    else:
        print(f"Hoy {response} ayusing mo buhay mmo at magsagot ka na")
'''

#7
'''
queen = {'first_name':'elsa', 'last_name':'lava', 'age':'31', 'city':'binangonan'}
princess = {'first_name':'anna', 'last_name':'sevastapool', 'age':'28', 'city':'angono'}
mentor = {'first_name':'ryan', 'last_name':'holiday', 'age':'35', 'city':'dallas'}
people = [queen, princess, mentor]

for hooman in people:
    for data in hooman:
        print(f"{data}: {hooman[data].title()}")
    print("\n")
'''

#8
'''
pet_1 = {'animal':'turtle', 'owner':'eca'}
pet_2 = {'animal':'cat', 'owner':'biel'}
pet_3 = {'animal':'dog', 'owner':'oyie'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
'''

#9
'''
friends = {
    'felipe':'france',
    'allen':'new zealand',
    'philip':'japan',
    'renz':'europe',
    'eca':'germany'
}

for hooman in friends.keys():
    print(f"{hooman.title()} wants to go to {friends[hooman].title()}")
'''

#10
'''
fave_num = {
    'oyie':'8, 7',
    'allen':'9, 6',
    'philip':'17, 5',
    'renz':'21, 6',
    'eca':'20, 6'
}

for name,num in fave_num.items():
    print(f"For {name.title()} the best numbers are {num}")
'''

#11 NOT YET DONE
cities = {
    'manila':{
        'country':'philippines',
        'population':'3 million',
        'fact':'hell on earth'   
    },

    'tokyo':{
        'country':'japan',
        'population':'1.5 million',
        'fact':'banzai banzai' 
    },

    'taipei':{
        'country':'taiwan',
        'population':'10 million',
        'fact':'silicon valley of asia' 
    }
}

for city in cities.keys():
    print(f"\nCity: {city.title()}")
    print("Obtained data: ")
    for title, data in cities[city].items():
        print(f"\t {title.title()}: {data.title()}")