# Random Number Generator

Welcome to the **Random Number Generator Program**! This Python program generates a random number within a user-defined range, using an interactive and user-friendly interface with a fun typing effect.

---

## Program Demo

Below is a quick demo of the Random Number Generator program:
![8project](https://github.com/user-attachments/assets/43ec2d84-d760-4cfd-aac5-4c0fc4a347cd)

---

## 🚀 Features

- **Typing Effect:** Displays text character by character for an engaging user experience.
- **Clear Screen Function:** Keeps the terminal clean and focused.
- **Range Validation:** Ensures the lower bound is less than the upper bound.
- **Random Number Generation:** Generates a random number within the specified range using Python's `random` module.
- **Repeatable Session:** Allows users to generate multiple random numbers until they choose to exit.
- **Graceful Exit:** Ends the program with a thank-you message.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Taking user input and displaying outputs interactively.
3. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To implement the typing effect.
   - `random`: To generate random numbers.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 08_Random_Number_Generator
   ```

2. **Run the Program:**
   Ensure you have Python installed on your system. Execute the script using:
   ```bash
   python random_number_generator.py
   ```

3. **Follow the Prompts:**
   - Enter the lower and upper bounds of the range.
   - View the randomly generated number.
   - Decide whether to generate another number or exit the program.

---

## Code Explanation

The main logic is implemented in the `random_number_generator` function:

1. **`clear_screen()`**: Clears the console for a seamless user experience.
2. **`typing(message, delay)`**: Simulates typing text with a delay.
3. **`hold_screen()`**: Pauses the screen until the user presses Enter.
4. **`get_range()`**:
   - Prompts the user for the lower and upper bounds.
   - Ensures the lower bound is less than the upper bound and validates input.
5. **`generate_random_number(lower, upper)`**:
   - Uses `random.randint()` to generate a random number within the specified range.
6. **`random_number_generator()`**:
   - Manages the program flow, including generating numbers, handling user input, and determining when to exit.

---

## Example Output

```plaintext
Welcome to the Random Number Generator!
Press Enter to continue...

Enter the lower bound of the range:
10
Enter the upper bound of the range:
100
Generating a random number between 10 and 100...
Your random number is: 42
Do you want to generate another random number? (yes/no)
yes

Enter the lower bound of the range:
1
Enter the upper bound of the range:
50
Generating a random number between 1 and 50...
Your random number is: 7
Do you want to generate another random number? (yes/no)
no
Thanks for using the Random Number Generator! Goodbye!
```

---

## 🚑 Acknowledgements

This program was designed as a fun way to practice Python input handling, error validation, and working with random numbers. It’s a great project for beginners learning Python.

---

Enjoy Coding! 🎲
