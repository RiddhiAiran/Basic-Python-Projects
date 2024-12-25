# Python Blackjack Game

Welcome to the **Python Blackjack Game**! This program is a fun and interactive way to play the classic card game of Blackjack directly in your terminal. Compete against the dealer and see if you can hit 21 without going over!

---

## 🚀 Features

- **Dynamic Gameplay**: The game automatically handles card dealing, scoring, and dealer actions.
- **User Interaction**: Users can decide to "hit" or "pass" based on their current score.
- **Automatic Dealer Play**: The dealer follows standard Blackjack rules to play until their score is at least 17.
- **Score Calculation**: Handles special rules for Aces (11 or 1 based on the hand's total score).
- **Detailed Game State**: Displays the user's cards, dealer's visible card, and final scores.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics**: Variables, Functions, Loops, and Conditionals.
2. **Input/Output**: Handling user inputs and displaying results interactively.
3. **Lists and Dictionary Usage**: Managing cards and operations like adding/removing elements.
4. **Random Module**: Generating random cards for a realistic gameplay experience.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 19_BlackJack
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python blackjack.py
   ```

3. **Follow the Prompts:**
   - Decide if you want to play a game.
   - During the game, choose to "hit" or "pass" based on your current score.
   - View the dealer's moves and the game's final outcome.

---

## 🃏 Gameplay Overview

1. **Dealing Cards**: The user and dealer each receive two cards.
2. **User's Turn**:
   - The user can "hit" (draw another card) or "pass" (end their turn).
   - The user's score is calculated after every action.
3. **Dealer's Turn**:
   - The dealer automatically draws cards until their score is at least 17.
4. **Final Comparison**:
   - The user's and dealer's scores are compared to determine the winner.

---

## Example Output

```plaintext
Welcome to Blackjack! 🎲

Your cards: [10, 7], current score: 17
Dealer's first card: [5]

Type 'y' to get another card, 'n' to pass: n

Your cards: [10, 7], current score: 17
Dealer's cards: [5, 9, 3], score: 17

It's a draw! 🤝
```

---

## ⚙️ Code Structure

1. **`cards`**: A list of possible card values (including 11 for Aces).
2. **`calculate_score(hand)`**: Adjusts scores for Aces and calculates the total for a hand.
3. **`compare_scores(user_score, dealer_score)`**: Determines the winner based on the final scores.
4. **`deal_initial_cards(deck)`**: Deals two cards to both the user and dealer.
5. **`user_play(deck, user_cards, dealer_cards)`**: Handles the user's turn, allowing them to "hit" or "pass."
6. **`dealer_play(deck, dealer_cards)`**: Dealer's logic to draw cards until the score is at least 17.
7. **`display_game_state(user_cards, dealer_cards, show_all=False)`**: Displays the current state of the game.
8. **`blackjack()`**: Orchestrates the game, handling user inputs and displaying the final results.

---

## 🚑 Acknowledgements

This program was created as a fun and engaging way to practice Python programming concepts like loops, conditionals, and randomization. It’s a great project for beginners and those looking to refine their coding skills.

---

Enjoy Coding and Good Luck! 🃏🎉

