import random
from .data import data
from .art import vs

def get_instagram_user():
    """
    Get a user from the presupplied data
    Return its dict
    """
    user = random.choice(data)
    return user

def user_info(user):
    """
    Given a dict of user data
    Return data from dict
    """
    return user['name'], user['description'], user['country'], user['follower_count']

def matchup(user1, user2):
    """
    Given 2 users
    Print to stdout matchup for game
    """
    print(f'Compare A: {user1[0]}, a {user1[1]} from {user1[2]}.')
    print(vs)
    print(f'Against B: {user2[0]}, a {user2[1]} from {user2[2]}.')
