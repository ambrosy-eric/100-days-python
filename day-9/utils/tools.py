bids = {}

def check_bids(dictionary):
    """
    Given a dictionary of bidders and bid amounts
    Determine who had the highest bid
    Return a dictionary of the highest bidder and bid
    """
    winning_bid = {}
    highest_bid = 0.0
    for bidder in dictionary:
        if dictionary[bidder] > highest_bid:
            highest_bid = round(dictionary[bidder], 2)
            winning_bid = {}
            winning_bid[bidder] = dictionary[bidder]
    return winning_bid
