tresure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

def main():
    print(tresure)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    path_choice = input('You come to a fork in the trail, do you go left or right?\n')
    if path_choice.lower() == 'left':
        river = input('You now find yourself at a river. Do you try to swim across, or wait?\n')
        if river.lower() == 'wait':
            print('You now come to an cave with three doors. A yellow door, a blue door, and a red door.')
            door = input('Which color door do you wish to open?\n')
            if door.lower() == 'yellow':
                print('You have found the treasure')
                print(tresure)
            elif door.lower() == 'red':
                print('You open the door and a swarm of bees fly out at you.\nGAME OVER')
            elif door.lower() == 'blue':
                print('You open the door and a curious aroma fills the room, making you extremely sleepy.\nGAME OVER')
        else:
            print('The current picks up as you try to swim across, you struggle, but are swept away by the current.\nGAME OVER')
    else:
        print('You have turned into the den of some hungry looking jaguars.\nGAME OVER')
    

if __name__ == "__main__":
    main()