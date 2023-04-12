'''
Lecture 8: Functions
This is a practice module for importing functions and such into a separate file.
'''

def print_friends(friend):
    for hooman in friend:
        print(hooman.title())

def greetings(friends):
    for friend in friends:
        print(f"Hello {friend.title()} tara lugaw tayo")