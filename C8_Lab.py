'''
Lab Chapter 8: Functions
Date: 01/27/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Defining a function
    2. Passing arguments
    3. Return values
    4. Passing a list
    5. Passing an arbitrary number of arguments
    6. Storing functions in modules
'''
# 1
'''
def display_message():
    print("For this module we are learning about the fundamentals of Python functions and the different methods to call it. ")

display_message()
'''

#2
'''
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


book = input("What is the title of your favorite book: ")
favorite_book(book)
'''

#3 
'''
def shirt_order(size, text):
    print(f"You ordered a size {size} which contains the text {text.title()}")

shirt_order(12,"i want to break free")
'''

#5
'''
def describe_city(city, country):
    print(f"{city.title()} is from {country.title()}")

describe_city('new york', 'usa')
'''

#6
'''
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country('manila', 'philippines')
'''

#7
'''
def make_album(name, title):
    catalog = {'Band Name': name.title(), 'Album Title': title.title()}
    return catalog

print(make_album('beatles', 'apple'))
'''

#8
'''
def make_song(name, title):
    catalog = {'Band Name': name.title(), 'Song Title': title.title()}
    return catalog

catalog_active = True

while catalog_active:
    band = input("What is your favourite band: ")
    if band == "q":
        break
    song = input("What is your favourite song: ")
    if song == "q":
        break

    print(make_song(band, song)) # the inputs will be printed as long as the input is not 'q'
'''

#9
'''
def chat(messages):
    for message in messages:
        print(message)

messages = ['tara bike', 'tara jogging', 'lugaw pre']
chat(messages)
'''

#11
'''
def send_chat(messages):
    while messages:
        data = messages.pop()
        print(data)
        sent_chat.append(data)

messages = ['tara bike', 'tara jogging', 'lugaw pre']
sent_chat = []
archive = messages[:]
send_chat(messages)
print(f"Messages list: {messages}")
print(f"Sent messages list: {sent_chat}")
print(f"Archived messages list: {archive}")
'''

#12
'''
def order(*contents):
    print("The contents of the sandwich are:")
    for item in contents:
        print(f"\t{item}")
order('burger', 'cheese', 'ham', 'lettuce')
'''

#13
'''
def build_profile(first, last, **user_data):
    user_data["first_name"] = first
    user_data["last_name"] = last
    return user_data

user = build_profile('biel', 'lava', best_camera = 'dslr', best_bike = "gravel" )
print(user)

#14 (not yet doner)
def make_car(manufacturer, model_name, **car_data):
    car_data["factory"] = manufacturer
    car_data["model_name"] = model_name
    return car_data
car = make_car()
'''











