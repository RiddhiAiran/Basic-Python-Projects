# Love Calculator

Welcome to the **Love Calculator**! This program calculates a "love score" between two names based on the occurrence of specific letters, making for a lighthearted and entertaining experience.

---

## Program Demo
Here’s a quick demonstration of the Love Calculator in action:


---

## 🚀 Features

- **Interactive Input:** Accepts two names as input to calculate a love score.
- **Clear Output:** Displays a two-digit love score derived from the logic.
- **Reusable Logic:** Modular design allows easy extension or modification of the scoring algorithm.
- **Simple and Fun:** A playful way to engage users with Python programming.

---

## 📚 Concepts Used

This program employs the following Python concepts:

1. **String Manipulation:** Combines and analyzes input strings.
2. **List Comprehension:** Efficiently counts occurrences of specific letters.
3. **Loops and Functions:** Keeps the program modular and organized.
4. **Interactive User Experience:** Handles user input and displays results dynamically.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 15_Love_Calculator
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python love_calculator.py
   ```

3. **Follow the Prompts:**
   - Enter your name and your partner's name.
   - Receive a fun love score!

---

## Code Explanation

### Main Functions

1. **`calculate_love_score(name1, name2)`**:
   - Combines the two input names and converts them to lowercase.
   - Counts occurrences of letters from the words "TRUE" and "LOVE."
   - Calculates and combines scores into a two-digit number.

2. **`main()`**:
   - Manages program flow, prompting the user to calculate a love score or exit.
   - Calls `calculate_love_score()` when appropriate.

---

## Example Output

```plaintext
Do you want to calculate your love? (y/n): y
Enter Your Name: Alice
Enter your Partner Name: Bob
Love Score: 23
```

---

## 🚑 Acknowledgements

This program was created as a fun way to practice Python programming concepts such as string manipulation and modular coding. It's a beginner-friendly project for developing interactive applications.

---

Enjoy Coding! ❤️
