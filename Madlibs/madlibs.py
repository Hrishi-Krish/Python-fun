import random

x = random.randint(0,2)
if x == 0:
    adj1 = input("Adjective: ")
    obj1 = input("Object: ")
    verb1 = input("Verb: ")
    obj2 = input("Object: ")

    print(f"It's a hot day, It's a {adj1} drink. Beads of {obj1} are {verb1}ing closer and closer and closer to the surface of the {obj2}")
else:
    day1 = input("Day: ")
    person1 = input("Person: ")
    event1 = input("Event: ")
    verb1 = input("Verb: ")
    anim = input("Animal or Bird: ")

    print(f"It was {day1} at school, and {person1} was super excited for {event1}. But when {person1} went outside to {verb1}, a {anim} stole {person1}'s pizza! {person1} chased the {anim} all over school.")