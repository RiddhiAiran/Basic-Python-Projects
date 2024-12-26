from data import data, vs, logo
import random
from common_functions import typing, hold_screen, clear_screen, get_input

def random_celeb(celeb_list):
    """Returns a random celebrity from the list."""
    return random.choice(celeb_list)


def higher_lower_game():
    """Main game logic for the Higher or Lower game."""
    A = random_celeb(data)
    B = random_celeb(data)
    
    # Ensure B is different from A
    while B == A:
        B = random_celeb(data)
    
    score = 0
    status = True

    while status:
        clear_screen()  # Clear screen for a cleaner UI (if supported)
        print(logo)
        
        # Display the score at the top of the screen
        if score > 0:
            print(f"Current score: {score}")
        
        typing(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
        print(vs)
        typing(f"Against B: {B['name']}, a {B['description']} from {B['country']}.")
        
        guess = get_input("\nWho has more followers? Type 'A' or 'B': ").strip().upper()

        # Check the guess
        if guess == 'A':
            is_correct = A['followers_count'] > B['followers_count']
        elif guess == 'B':
            is_correct = A['followers_count'] < B['followers_count']
        else:
            typing("Invalid input! Please type 'A' or 'B'.\n")
            continue

        # Handle correctness
        if is_correct:
            score += 1
            # Update A and B for the next round
            A = B
            B = random_celeb(data)
            
            # Ensure B is different from A
            while B == A:
                B = random_celeb(data)
        else:
            typing(f"Wrong! Game over. Final score: {score}\n")
            status = False


if __name__ == "__main__":
    higher_lower_game()
