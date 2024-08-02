#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
#Task 3: default path
    else:
        pass
elif place == "cave":
    #Task 2: setting the scene
    action = input("Would you like to light a torch or procced in the dark?")
    if action == 'light a torch':
        print("You find a hidden treasure!")
    elif action == 'procced in the dark':
        print("You trip and fall over the tresure chest! But at least you found it!")
    else:
        pass
else:
    pass