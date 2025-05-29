import time
import sys

health = 100
strength = 20
belongings = []

def entry():
    title = "-"*20 + " The Echoes of Eldoria " + "-"*20
    for char in title:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
def scene_1():
    scene1_begin = "-"*15 + " Scene 1: The Awakening " + "-"*15
    text_1 = "You wake up in a forest clearing. A soft voice whispers:\nOnly the worthy may return. Seek the Crystal. Choose your path:"

    paths_scene_1 = ["1. Go North towards the mountains.", "2. Go east into a glowing forest.", "3. Go west where ruins peek through the mist.", "4. Stay put and search the area"]

    dialogues = [scene1_begin, text_1]

    for dialogue in dialogues:
        for char in dialogue:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
    
    for path in paths_scene_1:
        print(path)
    
    user_choice = int(input("Choose your path: "))
    if user_choice == 1:
        scene_2A()

    

def scene_2A():
    scene_2A_begin = "-"*15+" Mountains of Mourn "+"-"*15
    
    for char in scene_2A_begin:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
    
    text_1 = "Harsh weather...You lose 10 health"
    text_2 = "You find a silver dagger lodged in a stone.\nTry to pull it out? "
    text_3 = "A mountain beast confronts you."

    print()

    print(text_1)
    global health
    health = health - 10
    if health <=0:
        print("You died!")
        sys.exit()
    print("Remaining health: %d" %health)

    time.sleep(0.5)
    
    print()

    print(text_2)
    global belongings
    global strength
    user_choice = input().lower()
    if user_choice == 'y':
        if strength > 15:
            belongings.append("Silver Dagger")
        else:
            print("Not enough strength. Required: %d, Your strength: %d" % (15, strength))
            print("You move on")

    time.sleep(0.5)

    print()

    print(text_3)
    if "Silver Dagger" in belongings:
        print("You take out the silver dagger. The bear runs away scared!")
    else:
        print("The mountain beast attacks. You lose 20 health")
        health = health-20
        if health <= 0:
            print("You died!")
            sys.exit()
    

entry()
scene_1()