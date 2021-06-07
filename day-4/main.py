import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def player_result():
    """
    Given a choice of rock, paper or scissors
    Return the correct variable
    """
    player_choice = input('What do you choose? Rock, Paper, Scissorss\n')
    valid_choices = ['rock', 'paper', 'scissors']
    if player_choice.lower() in valid_choices:
        if player_choice.lower() == 'rock':
            return rock
        if player_choice.lower() == 'paper':
            return paper
        else:
            return scissors
    else:
        raise Exception('Please choose rock, paper or scissors')

def computer_result():
    """
    Given a choice of rock, paper or scissors
    Return a random result
    """
    choice = random.randint(0,2)
    if choice == 0:
        return rock
    if choice == 1:
        return paper
    if choice == 2:
        return scissors

def outcome(choice1, choice2):
    """
    Given two choices
    Return the outcome
    """
    if choice1 != choice2:
        if choice1 == rock:
            if choice2 == paper:
                return 'You lose'
            if choice2 == scissors:
                return 'You win!'
        if choice1 == paper:
            if choice2 == rock:
                return 'You win!'
            if choice2 == scissors:
                return 'You lose'
        if choice1 == scissors:
            if choice2 == rock:
                return 'You lose'
            if choice2 == paper:
                return 'You win!'
    else:
        return 'Draw'

def main():
    player = player_result()
    print(f'You chose: \n{player}')
    computer = computer_result()
    print(f'Computer chose: \n{computer}')
    result = outcome(player, computer)
    print(result)
    
if __name__ == "__main__":
    main()