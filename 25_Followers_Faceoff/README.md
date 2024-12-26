```markdown
# 🎭 Higher or Lower Game

Welcome to the **Higher or Lower Game**! Test your knowledge of celebrities and social media by guessing who has more followers. Can you set a new high score?

---

## 📝 Description

The game pits two randomly selected celebrities against each other, and your goal is to guess which one has more followers on social media. With each correct guess, your score increases, and the challenge continues with a new comparison. Make a wrong guess, and the game ends!

---

## 🚀 Features

- 🧑‍🤝‍🧑 Compare celebrities based on their social media followers.
- 🎮 Tracks and displays your score dynamically.
- 🔄 Continuous play until a wrong guess.
- 🖼️ Visual aids with logos and comparison icons.
- 🎉 Fun and engaging!

---

## 🔧 Requirements

- Python 3
- A module named `common_functions` with the following functions:
  - `typing`: Displays text with typing animation.
  - `hold_screen`: Pauses the screen until the user presses a key.
  - `clear_screen`: Clears the console screen.
  - `get_input`: Safely handles user input.
- A module named `data` with:
  - `data`: A list of dictionaries, where each dictionary contains details about a celebrity (name, description, country, and followers_count).
  - `vs`: Visual representation (e.g., an ASCII art or string) for "versus."
  - `logo`: Visual representation (e.g., an ASCII art or string) for the game logo.

---

## 🛠️ Setup and Installation

1. Clone or download the repository containing the script and necessary assets.
2. Ensure that Python 3.12 is installed on your system.
3. Verify that the `common_functions` and `data` modules are available in the same directory as the script.
4. Run the program using the following command:
   ```bash
   python app.py
   ```

---

## 🕹️ How to Play

1. Start the game, and you'll be presented with two celebrities, **A** and **B**.
2. Read their descriptions and guess who has more followers:
   - Type `'A'` if you think celebrity A has more followers.
   - Type `'B'` if you think celebrity B has more followers.
3. If your guess is correct:
   - Your score increases.
   - Celebrity B becomes the new Celebrity A, and a new Celebrity B is chosen.
4. If your guess is wrong:
   - The game ends, and your final score is displayed.
5. Restart the game to play again.

---

## 📂 Code Explanation

### Functions

1. **`random_celeb(celeb_list)`**:
   - Selects a random celebrity from the provided list.

2. **`higher_lower_game()`**:
   - Main logic of the game:
     - Chooses two random celebrities for comparison.
     - Validates the player's guess.
     - Updates the score and celebrities dynamically.
     - Ends the game when the guess is incorrect.

---

## 👾 Example Output

```
🎭 Higher or Lower Game 🎭

Compare A: Taylor Swift, a singer from the USA.
vs
Against B: Cristiano Ronaldo, a football player from Portugal.

Who has more followers? Type 'A' or 'B': B

🎉 Correct! Current score: 1
...

Compare A: Cristiano Ronaldo, a football player from Portugal.
vs
Against B: Kylie Jenner, a model from the USA.

Who has more followers? Type 'A' or 'B': A

❌ Wrong! Game over. Final score: 1
```

---

## 📜 License

This project is licensed under the MIT License.

---

Put your celebrity knowledge to the test and have fun! 🌟
```