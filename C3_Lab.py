'''
Lab Chapter 3: Introducing Lists
Date: 01/19/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Accessing list elements
    2. Modifying list elements
    3. Adding list elements
    4. Removing list elements
'''
#1
'''
friends = ['oyie', 'allen', 'philip', 'renz']
print(f"\n{friends[0].title()} \n{friends[1].title()} \n{friends[2].title()} \n{friends[3].title()} ")
'''

#2
'''
friends = ['oyie', 'allen', 'philip', 'renz']
print(f"Tara na bike na {friends[0].title()}")
print(f"Tara na baseball na {friends[1].title()}")
print(f"Tara na gym na {friends[2].title()}")
print(f"Tara na welding na {friends[3].title()}")
'''

#4
'''
dinner_guests = ['adam savage', 'peter mckinnon', 'ryan holiday', 'robert greene']
print(f"I would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"Hello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"Hello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")
'''

#5
'''
dinner_guests = ['adam savage', 'peter mckinnon', 'ryan holiday', 'robert greene']
print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")
print("However it seems like Adam Savage is not available tonight therefore I must invite Jimmy Diresta instead")

dinner_guests[0] = 'jimmy diresta'

print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")
'''
#6
'''
dinner_guests = ['adam savage', 'peter mckinnon', 'ryan holiday', 'robert greene']
print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")
print("However it seems like Adam Savage is not available tonight therefore I must invite Jimmy Diresta instead")

dinner_guests[0] = 'jimmy diresta'

print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")

print("But hey I found a bigger table for us, would you mind if I invite more guests to join us?")

dinner_guests.insert(0, 'april wilkerson')
dinner_guests.insert(1, 'mayuko')
dinner_guests.append('seth')

#print(dinner_guests)

print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to talk about your CNC business")
print(f"\nHello {dinner_guests[1].title()} I would be honored to invite you since you inspired me to pursue programming")
print(f"\nHello {dinner_guests[2].title()} I would love to dine with you and discuss about your generalist approach to being a maker")
print(f"\nHello {dinner_guests[3].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[4].title()} I would love to invite you and {dinner_guests[5].title()} out for dinner to discuss more about stoicism and life in general")
print(f"\nHello {dinner_guests[6]} I would love to have you in my dinner party tonight")
'''

#7
'''
dinner_guests = ['adam savage', 'peter mckinnon', 'ryan holiday', 'robert greene']
print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")
print("However it seems like Adam Savage is not available tonight therefore I must invite Jimmy Diresta instead")

dinner_guests[0] = 'jimmy diresta'

print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to know about your shop ethos")
print(f"\nHello {dinner_guests[1].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[2].title()} I would love to invite you and {dinner_guests[3].title()} out for dinner to discuss more about stoicism and life in general")

print("But hey I found a bigger table for us, would you mind if I invite more guests to join us?")

dinner_guests.insert(0, 'april wilkerson')
dinner_guests.insert(1, 'mayuko')
dinner_guests.append('seth')

#print(dinner_guests)

print(f"\nI would like to invite you to dinner {dinner_guests[0].title()} since I would love to talk about your CNC business")
print(f"\nHello {dinner_guests[1].title()} I would be honored to invite you since you inspired me to pursue programming")
print(f"\nHello {dinner_guests[2].title()} I would love to dine with you and discuss about your generalist approach to being a maker")
print(f"\nHello {dinner_guests[3].title()} I would like to invite you to dinner to know more about you workflow in photography")
print(f"\nHello {dinner_guests[4].title()} I would love to invite you and {dinner_guests[5].title()} out for dinner to discuss more about stoicism and life in general")
print(f"\nHello {dinner_guests[6]} I would love to have you in my dinner party tonight")

print("\nFuck. I am sorry folks the delivery dude just called and notified me that the bigger table won't make it today")

trash = []

trash.append(dinner_guests.pop())
print(f"I am sorry {trash[0].title()} but you have to go")
trash.append(dinner_guests[1])
print(f"I am sorry {trash[1].title()} but you have to go too")'''

#8
places = ['japan', 'south korea', 'france', 'germany', 'england', 'norway', 'switzerland', 'canada', 'new york']
'''print('Here is the original list:')
print(places)
print('Here is the sorted list in alphabetical order')
print(sorted(places))
print('Here is the list in reverse alphabetical order')
print(sorted(places, reverse=True))'''
print('Here is the original list')
print(places)
print('Here is the reversed list')
print(places.reverse())
print('Now we can bring back the list into its original order')
print(places.reverse())

