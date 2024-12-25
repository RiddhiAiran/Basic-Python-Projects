# Hangman Game

Welcome to the **Hangman Game**! This program provides an engaging way to test your vocabulary and guessing skills through an interactive and fun game.

---

## Program Demo
Below is a quick demonstration of the Hangman Game in action:
![13project](https://github.com/user-attachments/assets/1e90c208-c0be-4422-8ca9-684f8a0690af)

---

## 🚀 Features

- **Typing Effect:** Displays text dynamically for a better user experience.
- **Clear Screen Functionality:** Keeps the terminal interface clean and easy to follow.
- **Word List Integration:** Randomly selects words for each game, ensuring variety.
- **Game Stages:** Visualizes the hangman stages for each incorrect guess.
- **Interactive Input:** Prompts the user for guesses, with validations and feedback.
- **Win/Loss Conditions:** Declares a win or loss based on the user's performance.

---

## 📚 Concepts Used

This program covers the following Python concepts:

1. **Modules and Imports:** Using both built-in and relative imports for structured code.
2. **Random Module:** Generates unpredictable word choices from the list.
3. **User Interaction:** Handles inputs and provides meaningful feedback.
4. **Loops and Conditionals:** Implements game logic for turns and win/loss conditions.
5. **String Manipulation:** Updates placeholders dynamically as the user guesses letters.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 13_Hangman
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python hangman.py
   ```

3. **Follow the Prompts:**
   - Decide whether to start a new game or exit.
   - Guess letters one at a time to reveal the hidden word.
   - Try to guess the entire word before running out of lives!

---

## Code Explanation

### Main Functions

1. **`game()`**:
   - Clears the screen and displays the game logo.
   - Chooses a random word and initializes placeholders for letters.
   - Manages the main game loop, including:
     - Processing user guesses.
     - Updating the hangman stages.
     - Declaring win or loss conditions.

2. **`main()`**:
   - Handles program entry and provides a menu for starting or exiting the game.
   - Calls the `game()` function if the user opts to play.

---

## Example Output

```plaintext
Welcome to Hangman Game!
Do you want to Play Hangman Game ? (y/n): y

Let's Play Hangman Game
Word to guess: _ _ _ _
Guess a letter: a
Good job! a is in the word.

************** 6/6 Lives Left ********************
```

---

## 🚑 Acknowledgements

This program was created as an educational project to enhance understanding of Python programming concepts like loops, conditionals, input validation, and modular design. Hangman is a great way to practice coding while building a fun game.

---

Enjoy Coding! 🎮
