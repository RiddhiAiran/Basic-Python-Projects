# Number Guessing Game

Welcome to the **Number Guessing Game**! Test your skills by guessing a randomly selected number between 1 and 100 within a limited number of attempts. Will you win or lose? Play now to find out!

---

## 🚀 Features

- **Custom Difficulty Levels**: Choose between `easy` (10 attempts) or `hard` (5 attempts).
- **Dynamic Feedback**: Receive real-time feedback if your guess is too high or too low.
- **Random Number Generation**: A new random number is generated every game to keep it exciting.
- **Interactive Gameplay**: Friendly prompts and clean user experience.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics**: Variables, Functions, Loops, and Conditionals.
2. **Input Handling**: Getting and validating user inputs.
3. **Random Module**: Generating random numbers.
4. **Functions**: Modular programming with clearly defined logic.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 20_Number_Guessing
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python number_guess.py
   ```

3. **Follow the Prompts:**
   - Select a difficulty level (`easy` or `hard`).
   - Guess the random number within the provided attempts.
   - Enjoy the game!

---

## 🕹️ Game Flow

1. **Game Start:**
   - The game welcomes you and generates a random number between 1 and 100.
   - You select the difficulty level: `easy` (10 attempts) or `hard` (5 attempts).

2. **Guessing Process:**
   - You make a guess and receive feedback:
     - `Too High!`: Your guess is greater than the random number.
     - `Too Low!`: Your guess is less than the random number.
     - `You Guessed it Right!`: You guessed the correct number.
   - The number of attempts is decremented after each guess.

3. **Game End:**
   - The game reveals the correct number and thanks you for playing.

---

## 🛠️ Code Explanation

### Key Functions:

1. **`level(input)`**:
   - Sets the number of attempts based on the difficulty level (`easy` or `hard`).

2. **`random_number()`**:
   - Generates a random integer between 1 and 100.

3. **`logic(random_digit, guess)`**:
   - Compares the guessed number with the random number and returns feedback (`Too High`, `Too Low`, or `Correct`).

4. **`game()`**:
   - Main logic of the game, including difficulty selection, guessing process, and feedback loop.

5. **`main()`**:
   - Handles the overall game flow, allowing users to replay or exit.

---

## Example Gameplay

```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You need to guess that number.

Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.

Make a guess: 50
Too Low!
You have 9 attempts remaining to guess the number.

Make a guess: 75
Too High!
You have 8 attempts remaining to guess the number.

Make a guess: 63
You Guessed it Right!

Correct Answer: 63
Thanks for playing!
```

---

## 🚑 Acknowledgements

This game was designed as an entertaining way to practice Python programming concepts like loops, conditionals, and random number generation. It’s a great beginner-friendly project for honing your skills.

---

Enjoy Coding! 🎉

