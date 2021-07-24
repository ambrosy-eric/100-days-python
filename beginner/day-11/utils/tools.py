import random

def deck():
    """
    Generic Deck of cards
    """
    cards = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    return cards

def deal(num):
    """
    Given an int number
    Deal that number of cards face up
    """
    deal = []
    while num != 0:
        deal.append(random.choice(list(deck().keys())))
        num -= 1
    return deal

def hand_value(hand):
    """
    Given a list as a blackjack hand
    Return its value
    If Ace is present and value is greater than 21
    Switch the Ace to a 1
    """
    value = 0
    for card in hand:
        value += deck()[card]
    if value > 21:
        if 'A' in hand:
            value -= 10
    return value

def check_bust(hand):
    """
    Given a Hand
    If more than 21
    Return True
    """
    value = hand_value(hand)
    if value > 21:
        return True

def play_blackjack(hand):
    """
    Given a hand
    Play blackjack with player
    Return hand & value
    """
    player_cycle = True
    while player_cycle:
        hit = input('Would you like to hit? (y/n)\n').lower()
        if hit == 'y':
            hand.append(deal(1)[0])
            print(f'Your hand is:\n{hand}')
            player_value = hand_value(hand)
            if check_bust(hand):
                return hand, hand_value(hand)
            print(f'You are sitting at {player_value}')
        else:
            player_cycle = False
    return hand, hand_value(hand)

def dealer_loop(hand):
    """
    Given a hand
    Run through dealer logic
    Returns hand & value
    """
    dealer_cycle = True
    while dealer_cycle:
        print(f'Dealer hand:\n{hand}')
        if hand_value(hand) < 17:
            print('Dealer with less than 17. Dealer must hit')
            hand.append(deal(1)[0])
        elif check_bust(hand):
            return hand, hand_value(hand)
        else:
            dealer_cycle = False
    return hand, hand_value(hand)
