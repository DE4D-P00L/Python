import random

r = random.randint(1, 9)

while 1:
    n = int(input("Enter Number: "))
    dist = n-r

    if dist == 0:
        print("Exactly Right!")
        break
    elif dist >= 3:
        print("Too High!")
    elif dist > 1:
        print("High!")
    elif dist <= -3:
        print("Too Low!")
    elif dist < -1:
        print("Low!")

    replay = input("Want to Continue (Y/N): ")
    print("")
    replay = replay.upper()

    if replay != "Y":
        print("You Quit!!!")
        break

