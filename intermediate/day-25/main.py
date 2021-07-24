from turtle import Screen
import turtle
import pandas as pd
from utils.tools import write_state

def main():
    screen = Screen()
    screen.title('US State Game')
    image = './utils/blank_map.gif'
    screen.addshape(image)
    turtle.shape(image)

    data = pd.read_csv('data/50_states.csv')
    states = data.state.str.lower()
    state_list = states.tolist()

    guessed_states = []

    while len(guessed_states) < 50:
        answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='Guess a state').lower()
        
        if answer == 'exit':
            missing_states = [state for state in state_list if state.capitalize() not in guessed_states]
            df = pd.DataFrame(missing_states)
            df.to_csv('data/states_missed.csv')
            break
        if answer in state_list:
            x = data.x[data.state.str.lower() == answer]
            y = data.y[data.state.str.lower() == answer]
            state = data.state[data.state.str.lower() == answer].item()
            write_state(state, int(x), int(y))
            guessed_states.append(state)

if __name__ == '__main__':
    main()
