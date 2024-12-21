# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors Game**! This Python program lets you play the classic game against the computer with a fun typing effect and an interactive interface.

---
## Program Demo

Below is a quick demo of the Rock, Paper, Scissors game:
![11project](https://github.com/user-attachments/assets/0dfeff65-3c9e-4a46-897d-28a0a91b5148)

---

## 🚀 Features

- **Typing Effect:** Displays text character by character for an engaging user experience.
- **Clear Screen Function:** Keeps the terminal clean and focused.
- **User-Friendly Input Validation:** Ensures valid choices for a seamless gaming experience.
- **Score Tracking:** Keeps track of the player's and computer's scores throughout the game.
- **Replay Option:** Allows users to play multiple rounds until they choose to exit.
- **Fun Visuals:** Includes ASCII art for rock, paper, and scissors.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Taking user input and displaying outputs interactively.
3. **Error Handling:** Validating and managing user inputs effectively.
4. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To implement the typing effect.
   - `random`: To generate the computer's choice randomly.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 11_Rock_Paper_Scissors
   ```

2. **Run the Program:**
   Ensure you have Python installed on your system. Execute the script using:
   ```bash
   python rock_paper_scissors.py
   ```

3. **Follow the Prompts:**
   - Enter your name.
   - Choose between rock, paper, or scissors (0, 1, or 2).
   - View the results of each round and the final scores.
   - Decide whether to play again or exit the game.

---

## Code Explanation

The main logic is implemented in the `play_game` function:

1. **`clear_screen()`**: Clears the console for a seamless user experience.
2. **`typing(message, delay)`**: Simulates typing text with a delay.
3. **`hold_screen()`**: Pauses the screen until the user presses Enter.
4. **`get_user_name()`**: Prompts the user for their name and ensures it's valid.
5. **`get_user_choice()`**:
   - Prompts the user to choose rock, paper, or scissors.
   - Validates the input to ensure it’s either 0, 1, or 2.
6. **`display_choices(user_choice, computer_choice, icons)`**:
   - Displays the choices made by the user and the computer using ASCII art.
7. **`determine_winner(user_choice, computer_choice)`**:
   - Compares the choices and determines the winner of the round.
8. **`play_game()`**:
   - Manages the entire game flow, including score tracking, replay logic, and displaying results.

---

## Example Output

```plaintext
Welcome to 🪨 Rock, 📄 Paper, ✂ Scissors!
What's your name?
Alice
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0
You chose:
    _______
---'   ____)        
      (_____)       
      (_____)       
      (____)        
---.__(___)  
       
Computer chose:
    _______
---'   ____)____    
          ______)   
          _______)  
         _______)   
---.__________)     
Computer won this round!
Do you want to play again? (yes/no)
no
Thanks for playing!
Here are the Final Scores: Alice 0 - 1 Computer
See you next time!
```

---

## 🚑 Acknowledgements

This program was designed as a fun way to practice Python fundamentals while enjoying a classic game. It’s perfect for beginners looking to enhance their coding skills.

---

Enjoy Gaming! 🎮
