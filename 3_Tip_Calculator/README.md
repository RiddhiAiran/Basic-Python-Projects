# Tip Calculator

Welcome to the **Tip Calculator**! This Python program helps you calculate how much each person should pay when splitting a bill, including a tip, using an interactive and user-friendly interface.

---

## Program Demo

Below is a quick demo of the Tip Calculator program:


---

## 🚀 Features

- **Typing Effect:** Displays text character by character for a smooth and engaging user experience.
- **Clear Screen Function:** Automatically clears the terminal to keep the interface clean and focused.
- **Tip Calculation:** Allows you to add a customizable tip percentage to your bill.
- **Bill Splitting:** Splits the total bill, including the tip, among a specified number of people.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Handling user inputs and printing outputs.
3. **String Manipulation:** Formatting strings dynamically to display results.
4. **Control Flow:** Managing program logic through function calls and conditionals.
5. **Modules:**
    - `os`: For clearing the terminal screen.
    - `time`: To implement the typing effect.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 3_Tip_Calculator
   ```

2. **Run the Program:**
   Ensure you have Python installed on your system. Execute the script using:
   ```bash
   python tip_calculator.py
   ```

3. **Follow the Prompts:**
   - Enter the total bill amount.
   - Specify the tip percentage (10, 12, or 15).
   - Input the number of people to split the bill with.

---

## Code Explanation

The main logic is implemented in the `tip_calculator` function:

1. **`clear_screen()`**: Clears the console for a seamless user experience.
2. **`typing(message, delay)`**: Simulates typing by displaying one character at a time with a delay.
3. **`tip_calculator()`**:
   - Prompts the user for input (total bill, tip percentage, and number of people).
   - Calculates the total bill with tip and the amount each person should pay.
   - Displays the results in a formatted manner.

---

## Example Output

```plaintext
🧾 Welcome to the Tip Calculator! 😇

💵 What was the Total Bill? $100
📝 How much tip would you like to give? 10, 12, or 15? : 15
🧑‍🧑‍🧒‍🧒 How many people to split the bill? (at least 1) : 4
----------------------------------------------------------------------

Your Total Bill with Tip Would be : $115.0

Each person should pay: $28.75
```

---

## 🚑 Acknowledgements

This project was inspired by everyday scenarios where splitting bills and calculating tips becomes tedious. The program provides a quick and easy solution!

---

Happy Coding! 🎉
