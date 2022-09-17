from replit import clear
from art import logo

#TODO-1 Display logo from art.py
print(logo)
print('Welcome to the secret auction program.')

#e.g {'Alan': 100, 'Alex': 200}
bids = {}
should_continue = True


def find_highest(bidders):
    highest_price = 0
    winner = ''
    for name in bidders:
        if bidders[name] > highest_price:
            highest_price = bidders[name]
            winner = name
    return winner


while should_continue:
    #e.g 'Alan': 100
    #TODO-2 Ask for Name input
    name = input('What is your name? ')
    #TODO-3 Ask for Bid price
    bid_price = int(input('What is your bid? $'))
    #TODO-4 Add name and bid_price into a dict as the key and value
    bids[name] = bid_price

    #TODO-5 Ask if there are other users who want to bid
    other_bidder = input("Are there any other bidders? Type 'yes' or no: ")
    if other_bidder == 'no':
        should_continue = False
        winner = find_highest(bids)
        print(f"The winner is {winner} with a bid of ${bids[winner]}")
    elif other_bidder == 'yes':
        clear()
