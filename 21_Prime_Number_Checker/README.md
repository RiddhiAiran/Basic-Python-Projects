# Prime Number Checker

Welcome to the **Prime Number Checker**! This Python program allows you to determine whether a number is prime or not. A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

---

## 🚀 Features

- **User-Friendly Interface:** Provides an intuitive way to input numbers and view results.
- **Efficient Logic:** Quickly checks for primality using a simple loop.
- **Replay Option:** Allows users to check multiple numbers in one session.

---

## 📚 Concepts Used

1. **Prime Number Logic:** Checks divisibility from 2 up to the number minus 1.
2. **Input Handling:** Ensures the user provides a valid integer.
3. **Functions:** Encapsulates functionality in reusable blocks.
4. **Loop Control:** Manages repeated primality checks based on user input.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 21_Prime_Number_Checker
   ```

2. **Run the Program:**
   Make sure Python is installed on your system. Execute the script using:
   ```bash
   python prime_number.py
   ```

3. **Follow the Prompts:**
   - Enter the number you want to check for primality.
   - Receive a result indicating whether the number is prime or not.

---

## 🛠️ Code Explanation

### Main Functions

1. **`is_prime()`**:
   - **Purpose:** Checks whether a number is prime.
   - **Logic:**
     - Loops from 2 to the number minus 1.
     - Returns `False` if the number is divisible by any value in this range.
     - Returns `True` otherwise.

2. **`main()`**:
   - **Purpose:** Handles the overall program flow.
   - **Features:**
     - Prompts the user to check for a prime number.
     - Calls `is_prime()` and displays the result.
     - Allows users to replay or exit the program.

---

## Example Output

```plaintext
Welcome to the prime number checker!
Enter your number: 13
It's a Prime Number.

Do you want to check whether a number is prime or not? (y/n): y
Enter your number: 12
It's not a Prime Number.

Do you want to check whether a number is prime or not? (y/n): n
Good Bye! See You.
```

---

## 🚑 Acknowledgements

This program was created as a simple and interactive way to learn Python basics and understand primality testing. It’s an excellent project for beginners to strengthen their coding skills.

---

Enjoy coding and exploring mathematics with Python! ✨
