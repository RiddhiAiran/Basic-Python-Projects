from .logo import logo
from common_functions import typing, hold_screen, clear_screen, get_input

def highest_bid(bidders):
    """Calculates the Highest Bid"""
    max_bid = 0
    winner_name = ''
    for name,value in bidders.items(): 
        if max_bid < value:
            max_bid = value
            winner_name = name
    return max_bid, winner_name

def auction():
    """Main Logic of the Bidding Program"""
    clear_screen()
    typing("Welcome to the Secret Auction!\n")
    bidders = {}
    while True:
        print(logo)
        name = get_input("What is your name?: ")
        bid = get_input("What's Your Bid : $",is_float=True)
        bidders[name] = bid
        status = get_input("Are there any other bidders? Type 'yes or 'no' : ").lower()
        if status not in ["yes","y"]:
            clear_screen()
            print(logo)
            winner_bid, winner_name = highest_bid(bidders)
            typing(f"The winner of this auction is {winner_name} with a bid of ${winner_bid}\n")
            hold_screen()
            break
        clear_screen()

def main():
    """Main Function to Run the Auction"""
    while True:
        clear_screen()
        participate = get_input("Do you want to Participate in the Secret Auction ? (y/n): ").lower()
        if participate == 'y':
            hold_screen()
            auction()
        else:
            typing("Good Bye! Have a Nice Day\n")
            break

if __name__ == '__main__':
    main()