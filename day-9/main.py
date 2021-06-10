from replit import clear
from utils.art import logo
from utils.tools import bids, check_bids

def main():
    print(logo)
    additional_bidders = True
    while additional_bidders:
        name = input('What is your name?\n')
        bid = float(input('How much money would you like to bid?\n$'))
        bids[name] = bid
        if input('Are there others who wish to bid? (Yes/No)\n').lower() == 'yes':
            clear()
        else:
            clear()
            additional_bidders = False
    winning_bid = check_bids(bids)
    for bidder in winning_bid:
        highest_bidder = bidder
        highest_bid = winning_bid[bidder]
    print(f'Winner: {highest_bidder}\nWinning Bid: ${highest_bid}\nThanks for bidding!')
    

if __name__ == '__main__':
    main()
