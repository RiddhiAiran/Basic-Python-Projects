# Online Pizza Order Machine

Welcome to the **Online Pizza Order Machine**! This Python program automates your pizza ordering experience by guiding you through size selection, toppings, and calculating the final bill—all with an interactive interface and typing effect.

---

## Program Demo

Below is a quick demo of the Online Pizza Order Machine program:
![6project](https://github.com/user-attachments/assets/2679ec89-b042-4fa0-9613-a6e92ac95820)


---

## 🚀 Features

- **Typing Effect:** Text is displayed character by character for an engaging and interactive user experience.
- **Clear Screen Function:** Clears the terminal to keep the interface clean and focused.
- **Pizza Ordering:**
   - Choose pizza size: Small, Medium, or Large.
   - Add optional toppings like Pepperoni and Extra Cheese.
   - Automatic calculation of the total bill.
- **Repeatable Orders:** Easily order multiple pizzas in one session.
- **Graceful Exit:** Option to quit the program when you’re done.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Handling user inputs and printing outputs.
3. **String Manipulation:** Dynamically formatting strings to display results.
4. **Control Flow:** Managing program logic through functions, loops, and conditionals.
5. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To create the typing effect.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 06_Pizza_Delivery_Order
   ```

2. **Run the Program:**
   Ensure you have Python installed on your system. Execute the script using:
   ```bash
   python pizza_delivery_order.py
   ```

3. **Follow the Prompts:**
   - Enter your name.
   - Select the size of the pizza (S, M, or L).
   - Choose optional toppings (Pepperoni and Extra Cheese).
   - View your final bill.
   - Optionally, order another pizza or exit.

---

## Code Explanation

The main logic is implemented in the `Pizza_Order` function:

1. **`clear_screen()`**: Clears the console for a clean user experience.
2. **`typing(message, delay)`**: Simulates typing by displaying one character at a time.
3. **`hold_screen()`**: Waits for the user to press Enter before proceeding.
4. **`Pizza_Order()`**:
   - Prompts the user for inputs: name, pizza size, pepperoni preference, and extra cheese preference.
   - Calculates the final bill based on inputs:
     - Small Pizza: $15 (+$2 for Pepperoni).
     - Medium Pizza: $20 (+$3 for Pepperoni).
     - Large Pizza: $25 (+$3 for Pepperoni).
     - Extra Cheese: +$1.
   - Displays the total bill.
   - Holds the screen until the user presses Enter.
5. **Loop for Multiple Orders**: The program keeps running until the user chooses to exit.

---

## Example Output

```plaintext
🍕🍕 Welcome to the Online Pizza Order Machine!🍕 
Enter your Name : JOHN
🫓 What Size Pizza do you want? S, M or L?: M
🥫 Do you want Pepperoni on your pizza? Y or N: Y
🧀 Do you want extra Cheese? Y or N: N
💵 Your Final Bill is : $23
Enjoy your Pizza! 🍕🍕
Press Enter to continue...

Do you want to Order a Pizza 🍕 ? (Y or N) : N
Good Bye!
```

---

## 🚑 Acknowledgements

This project was inspired by the joy of ordering pizzas online and automating the process for practice with Python. It’s a fun program for both learners and enthusiasts!

---

Happy Coding! 🎉
