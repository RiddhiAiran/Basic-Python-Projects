# Banker Roulette with Typing Effect

Welcome to the **Banker Roulette**! This program helps pick a random participant to pay the bill, adding fun and excitement to group outings. The interactive design makes it engaging and easy to use.

---

## Program Demo
Below is a quick demo of the Banker Roulette program:
![10project](https://github.com/user-attachments/assets/23365792-f9e2-4ab1-9de9-56ba56b770fe)

---


## 🚀 Features

- **Typing Effect:** Provides a dynamic and user-friendly text display.
- **Clear Screen Function:** Ensures a clean terminal interface for better focus.
- **Random Selection:** Uses the `random` module to fairly choose a participant from the list.
- **Validation:** Ensures at least two participants are entered for the game.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Handling user inputs and displaying outputs.
3. **List Manipulation:** Working with lists to store and process participant names.
4. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To implement the typing effect.
   - `random`: For selecting a random participant.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/basic-python-programs.git
   cd 10_Banker_Roulette
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python banker_roulette.py
   ```

3. **Follow the Prompts:**
   - Enter the names of participants separated by commas.
   - The program will randomly select a participant to pay the bill.

---

## Code Explanation

The main logic is implemented in the `banker_roulette` function:

1. **`clear_screen()`**: Clears the console to provide a clean interface.
2. **`typing(message, delay)`**: Simulates typing text with a delay for enhanced engagement.
3. **`hold_screen()`**: Pauses the program until the user presses Enter.
4. **`banker_roulette()`**:
   - Prompts the user to enter participant names separated by commas.
   - Validates the input to ensure at least two participants are entered.
   - Uses the `random.choice()` function to select a random participant from the list.
   - Displays the chosen participant as the "banker."

---

## Example Output

```plaintext
Welcome to the Banker Roulette!💵
👤👤👤 Enter the names of participants, separated by commas:
Alice, Bob, Charlie, Diana

The banker is 👤 : Diana! They will pay the bill this time. 🎉
```

---

## 🚑 Acknowledgements

This program was created to add a fun and interactive twist to bill-splitting scenarios. It demonstrates how Python can be used to create engaging and practical applications for everyday use.

---

Enjoy Coding! 🎉
