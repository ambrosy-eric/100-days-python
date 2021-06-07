### https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    """
    Need to turn right
    Turn left 3 times to face right from starting location
    """
    turn_left()
    turn_left()
    turn_left()
    
def face_north():
    """
    Determine what direction you are facing
    Reoriate yourself to face north and turn right open
    """
    while not is_facing_north():
        turn_left()
    if right_is_clear():
        turn_right()
    return
   
def main():
    face_north()
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

if __name__ == '__main__':
    main()