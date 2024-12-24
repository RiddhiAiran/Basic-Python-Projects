# Even and Odd Number Checker

Welcome to the **Even and Odd Number Checker Program**! This Python program lets you check whether a number is even or odd with an engaging user experience and a clean, interactive interface.

---

## Program Demo
Below is a quick demo of the Even and Odd Number Checker program:
![5project](https://github.com/user-attachments/assets/38e83e9f-94cd-419a-937c-772b551fe100)

---

## 🚀 Features

- **Typing Effect:** Displays text character by character to enhance user interaction.
- **Clear Screen Function:** Keeps the terminal clean for a focused experience.
- **Even/Odd Check:** Determines whether a number is even or odd using simple modular arithmetic.
- **Repeatable Session:** Allows users to check multiple numbers until they choose to exit.
- **Graceful Exit:** Ends the program with a thank-you message.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Handling user input and displaying results interactively.
3. **Control Flow:** Using `if-else` statements for decision-making.
4. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To implement the typing effect.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/basic-python-programs.git
   cd 05_Even_Odd_Checker
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python even_odd_checker.py
   ```

3. **Follow the Prompts:**
   - Enter the number you want to check.
   - View whether the number is even or odd.
   - Decide whether to check another number or exit the program.

---


## Code Explanation

The main logic is implemented in the `even_odd` function:

1. **`clear_screen()`**: Clears the console to provide a clean interface.
2. **`typing(message, delay)`**: Simulates typing text with a delay for better engagement.
3. **`hold_screen()`**: Pauses the program until the user presses Enter.
4. **`even_odd()`**:
   - Takes user input for a number.
   - Checks whether the number is even or odd using `num % 2 == 0`.
   - Displays the result with the typing effect.
5. **`while True` Loop:**
   - Allows users to check multiple numbers in one session.
   - Gracefully exits when the user chooses not to continue.

---

## Example Output

```plaintext
Welcome to the Even and Odd Number Checker!
Press Enter to continue...

Do you want to Check a Number is even or Odd? (y/n): y
Press Enter to continue...

Enter your Number: 42
42 is an Even Number
Press Enter to continue...

Do you want to Check a Number is even or Odd? (y/n): n
Thank you for Coming!
```

---

## 🚑 Acknowledgements

This program was created as a fun way to practice basic Python concepts, including conditionals, loops, and modular arithmetic. It’s a beginner-friendly project to enhance your Python skills.

---

Enjoy Coding! 🔢
