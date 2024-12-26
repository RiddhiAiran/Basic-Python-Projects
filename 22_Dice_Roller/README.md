```markdown
# 🎲 Dice Roller Game

Welcome to the **Dice Roller Game**! This simple Python program allows you to roll a virtual dice and see the result with an engaging user experience.

---

## 📝 Description

The Dice Roller Game simulates rolling a six-sided dice. Upon rolling, the program displays the result using emoji representations for each dice face. You can roll the dice as many times as you want or exit the game at any time.

---

## 🚀 Features

- 🎲 Simulates rolling a six-sided dice.
- ⏳ Provides an interactive experience with a small delay to simulate rolling.
- 📜 Displays the dice face with fun emojis for a better user experience.
- 🔁 Allows repeated rolls until the user decides to quit.

---

## 🔧 Requirements

- Python 3
- A module named `common_functions` with the following functions:
  - `typing`: Displays text with typing animation.
  - `hold_screen`: Pauses the screen until the user presses a key.
  - `clear_screen`: Clears the console screen.
  - `get_input`: Safely handles user input.

---

## 🛠️ Setup and Installation

1. Clone or download the repository containing the Dice Roller program.
2. Ensure that Python 3.12 is installed on your system.
3. Verify the `common_functions` module is available in the same directory as the script.
4. Run the program using the following command:
   ```bash
   python dice_roller.py
   ```

---

## 🕹️ How to Play

1. Run the program.
2. You will be prompted:
   ```
   Do you want to Roll a Dice? (y/n):
   ```
   - Type `y` to roll the dice.
   - Type `n` to exit the game.
3. If you choose to roll, the dice face result will be displayed:
   ```
   You Got: 🎲
   ```
4. You can continue rolling or exit at any time.

---

## 📂 Code Explanation

### Functions

1. **`roll()`**:
   - Clears the screen and displays a welcome message.
   - Simulates the dice roll by selecting a random emoji from the list of dice faces.
   - Displays the rolled dice face.
   - Waits for the user to continue.

2. **`main()`**:
   - Handles the main program flow.
   - Prompts the user to roll the dice or exit.
   - Repeats the dice rolling process until the user decides to quit.

---

## 👾 Example Output

```
Welcome to the Dice Roller!

Let's Roll a Dice....

You Got: 🎲
```

---

Enjoy the game and may the dice roll in your favor! 🎉
```