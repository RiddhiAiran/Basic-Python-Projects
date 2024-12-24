import random
from common_functions import typing, hold_screen, clear_screen, get_input
from .logo import logo, stages  # Relative import for logo and stages
from .words import word_list  # Relative import for word_list

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

        guess = get_input("Guess a letter: ").lower()

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

def main():
    """Main Function to Run the Game"""
    while True:
        clear_screen()
        status = get_input("Do you want to Play Hangman Game ? (y/n) : ").lower()
        if status == 'y':
            hold_screen()
            game()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break


if __name__ == '__main__':
    main()