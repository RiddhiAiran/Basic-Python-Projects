import random
from common_functions import typing, hold_screen, clear_screen, get_input

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 

def calculate_score(hand):
    """Calculate the score of a hand, adjusting for Aces."""
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1) # Convert Ace from 11 to 1
    return score

def compare_scores(user_score, dealer_score):
    """Compare user and dealer scores to determine the outcome."""
    if user_score > 21:
        return "You went over. You lose! 💥"
    elif dealer_score > 21:
        return "Dealer went over. You win! 🎉"
    elif user_score == dealer_score:
        return "It's a draw! 🤝"
    elif user_score == 21:
        return "Blackjack! You win! 🎰"
    elif dealer_score == 21:
        return "Dealer has Blackjack. You lose! 😔"
    elif user_score > dealer_score:
        return "You win! 🎊"
    else:
        return "You lose! 😤"

def deal_initial_cards(deck):
    """Deal two initial cards to the player and dealer."""
    user_cards = [random.choice(deck) for _ in range(2)]
    dealer_cards = [random.choice(deck) for _ in range(2)]
    return user_cards, dealer_cards

def deal_card(deck):
    """Deal a single card from the deck."""
    return random.choice(deck)

def dealer_play(deck, dealer_cards):
    """Dealer plays until the score is at least 17."""
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card(deck))
    return dealer_cards

def display_game_state(user_cards, dealer_cards, show_all=False):
    """Display the current state of the game."""
    user_score = calculate_score(user_cards)
    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    if show_all:
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer's cards: {dealer_cards}, score: {dealer_score}")
    else:
        print(f"Dealer's first card: [{dealer_cards[0]}]")

def user_play(deck, user_cards, dealer_cards):
    """Handle the user's turn."""
    while True:
        display_game_state(user_cards, dealer_cards)
        if calculate_score(user_cards) >= 21:
            break
            
        hit = get_input("Type 'y' to get another card, 'n' to pass: ").lower()
        if hit == 'y':
            user_cards.append(deal_card(deck))
        else:
            break
    return user_cards

def blackjack():
    """Main function to play the game of Blackjack."""
    clear_screen()
    typing("Welcome to Blackjack! 🎲\n")

    while True:
        play = get_input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play != 'y':
            typing("Thanks for playing! 👋\n")
            break
        hold_screen()
        clear_screen()
        user_cards, dealer_cards = deal_initial_cards(cards)

        # User's turn
        user_cards = user_play(cards, user_cards, dealer_cards)
        user_score = calculate_score(user_cards)

        # Dealer's turn
        if user_score <= 21:
            dealer_cards = dealer_play(cards, dealer_cards)
        
        dealer_score = calculate_score(dealer_cards)

        # Final results
        display_game_state(user_cards, dealer_cards, True)
        print("\n" + compare_scores(user_score, dealer_score))

if __name__ == "__main__":
    blackjack()