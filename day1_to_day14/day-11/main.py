import random
from utils.art import logo
from utils.tools import deck, deal, hand_value, play_blackjack, dealer_loop

def main():
    print(logo)
    player_hand = deal(2)
    print(f'Your hand is:\n{player_hand}')
    dealer_hand = deal(1)
    print(f'Dealer is showing:\n{dealer_hand}')
    dealer_hand.append(deal(1)[0])
    player_value = hand_value(player_hand)
    print(f'You are sitting at {player_value}')

    player = play_blackjack(player_hand)
    print(f'Your hand is:\n{player[0]}')
    print(player[1])
    if player[1] > 21:
        print(f'You have busted. Dealer wins.')
        return
    dealer = dealer_loop(dealer_hand)
    print(f'Dealer hand is:\n{dealer[0]}')
    if dealer[1] > 21:
        print('Dealer has busted.\nYou WIN!')
        return
    else:
        if player[0] > dealer[0]:
            print('You win!')
        else:
            print('Dealer wins.')

if __name__ == '__main__':
    main()
