import os 
import time
import random

from logo import logo, stages
from words import word_list

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

def game():
    """Hangman Game Logic"""
    clear_screen()
    print(logo)
    typing("Let's Play Hangman Game\n")
    hold_screen()
    clear_screen()

    choosen_word = random.choice(word_list)
    placeholder = ['_' for _ in choosen_word]
    typing(f"Hint : {choosen_word}")
    correct_letters = []
    lives = 6
    Game_Over = False

    while not Game_Over:
        print(logo)
        print(f"Word to guess: {' '.join(placeholder)}")
        print(f"************** {lives}/6 Lives Left ********************")

        typing("Guess a letter: ")
        guess = input().strip().lower()

        clear_screen()
        print(logo)

        if guess in correct_letters:
            typing(f"You've already guessed {guess}. Try again.")
        elif guess in choosen_word:
            typing(f"Good job! {guess} is in the word.")
            for idx, letter in enumerate(choosen_word):
                if letter == guess:
                    placeholder[idx] = guess
            correct_letters.append(guess)
        else:
            typing(f"You guessed {guess}, which is not in the word. You lose a life.")
            lives -= 1
            correct_letters.append(guess)

        print(stages[lives])
        if lives == 0:
            Game_Over = True
            print("************************ YOU LOSE **************************")
            typing(f"The word was: {choosen_word}")
            hold_screen()
        elif '_' not in placeholder:
            Game_Over = True
            print("************** YOU WIN ****************")
            hold_screen()

        if not Game_Over:
            hold_screen()
            clear_screen()


while True:
    clear_screen()
    typing("Do you want to Play Hangman Game ? (y/n) : ")
    status = input().strip().lower()
    if status not in ['y','yes']:
        typing("Good Bye!\n")
        break
    else:
        game()
