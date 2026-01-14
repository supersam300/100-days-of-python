import art
from os import system
print(art.hammer)
bidders = {}
name = input("enter the name of the bidder\n")
system("clear")
bid = int(input("enter the amout to bid\n"))
bidders[name] = bid
val = input("is there another bidder")

def max_bidder(bidders):
    max_bid = 0
    max_name = ''
    for people in bidders:
        if bidders[people] > max_bid:
            max_bid = bidders[people]
            max_name = people
    return max_name 

while val == 'yes':
    system("clear")
    name = input("enter the name of the bidder\n")
    system("clear")
    bid = int(input("enter the amout to bid\n"))
    bidders[name] = bid
    val = input("is there another bidder")
    if val == 'no':
        print(f"the winner is {max_bidder(bidders)}")

