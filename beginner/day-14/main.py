from utils.art import logo
from utils.tools import get_instagram_user, user_info, matchup

def main():
    score = 0
    keep_playing = True
    while keep_playing:
        print(logo)
        a = get_instagram_user()
        b = get_instagram_user()
        while a['name'] == b['name']:
            b = get_instagram_user()
        a_info = user_info(a)
        b_info = user_info(b)
        matchup(a_info, b_info)
        guess = input('Who has more followers? Type A or B: ').lower()
        try:
            if guess == 'a':
                if a_info[3] > b_info[3]:
                    score += 1
                    print(f'Thats correct! Your score is {score}')
                else:
                    break
            elif guess == 'b':
                if b_info[3] > a_info[3]:
                    score += 1
                    print(f'Thats correct! Your score is {score}')
                else:
                    break
        except Exception as e:
            print('Must choose either A or B')
    print(f'Sorry that is incorrect. Final score: {score}')


if __name__ == '__main__':
    main()
