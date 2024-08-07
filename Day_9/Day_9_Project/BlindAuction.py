from code import clear

from art import logo

print(logo)

auction_bids = {}
bid_ends = False

def finding_highest_bidder(bidding_data):
  highest_bid = 0
  winner = ""
  for bid in bidding_data:
    bid_amount = bidding_data[bid]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bid
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bid_ends:
  name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))
  auction_bids[name] = bid_amount
  more_bids = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if more_bids.lower() == "no":
    bid_ends = True
    finding_highest_bidder(auction_bids)
  elif more_bids.lower() == "yes":
    clear()
    