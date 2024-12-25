# Caesar Cipher Encoder/Decoder

Welcome to the **Caesar Cipher Program**! This tool lets you encrypt and decrypt messages using a simple Caesar cipher technique, providing a fun and interactive experience.

---

## Program Demo
Here’s a quick demo of how the Caesar Cipher works:

---

## 🚀 Features

- **Encryption and Decryption:** Easily switch between encoding and decoding messages.
- **Dynamic Typing Effect:** Displays messages character by character for enhanced interaction.
- **Input Validation:** Ensures valid inputs for options and shift values.
- **Case Insensitive:** Handles both uppercase and lowercase letters seamlessly.
- **Symbol and Space Handling:** Retains non-alphabetic characters in their original form.

---

## 📚 Concepts Used

This program utilizes the following Python concepts:

1. **Loops and Conditionals:** Implements logic for encoding and decoding.
2. **String Manipulation:** Updates characters based on shift values.
3. **Modular Programming:** Keeps the code structured and reusable with functions.
4. **Error Handling:** Ensures smooth handling of invalid inputs.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 14_Caesar_Cipher
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the Prompts:**
   - Choose to encode or decode your message.
   - Enter the text and shift value.
   - Receive the transformed output!

---

## Code Explanation

### Main Functions

1. **`caesar()`**:
   - Clears the screen and displays the logo.
   - Prompts the user to choose between encoding and decoding.
   - Takes the message and shift value as input.
   - Applies the Caesar cipher to transform the message.
   - Displays the resulting text.

2. **`main()`**:
   - Manages the program flow, providing a menu to start or exit the application.
   - Calls the `caesar()` function for encoding/decoding operations.

---

## Example Output

```plaintext
Welcome to the Caesar Cipher Program!
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 3
Here is the encode result: khoor zruog
```

---

## 🚑 Acknowledgements

This program was created to demonstrate the fundamentals of cryptography using Python. It’s an excellent beginner project for learning loops, conditionals, and string operations while having fun with ciphers.

---

Enjoy Coding! 🔐
