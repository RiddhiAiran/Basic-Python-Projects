# Generation Category Finder 🌟

This Python application determines your generational category based on your birth year. It's a fun and interactive way to learn about the generational classifications.

---

## Features 🚀
- **Interactive Experience**: Prompts users to input their birth year and displays the corresponding generational category.
- **Accurate Categorization**: Includes all major generations from "The Greatest Generation" to "Gen-Alpha."
- **User-Friendly Interface**: Clear instructions and seamless navigation between checking generations and exiting the program.

---

## How It Works 💡
1. The user is asked to enter their birth year.
2. The program matches the input year to a generation category:
   - **The Greatest Generation** (1901–1924)
   - **The Silent Generation** (1925–1945)
   - **The Baby Boomer Generation** (1946–1964)
   - **Generation X (Gen-X)** (1965–1979)
   - **The Millennials** (1980–1994)
   - **Generation Z (Gen-Z)** (1995–2009)
   - **Generation Alpha (Gen-Alpha)** (2010–2025)
3. Displays the corresponding category or asks for valid input if the year is out of range.
4. The user can choose to check another year or exit the program.

---

## Code Explanation 🧑‍💻

### Core Functions

1. **`generation()`**
   - Takes the user's birth year as input.
   - Matches the year to a generational category using a series of conditional statements.
   - Displays the generational category or an error message for invalid input.

2. **`main()`**
   - The main loop of the program.
   - Asks the user if they want to check their generation category.
   - Calls the `generation()` function if the user chooses to proceed.
   - Displays a farewell message on exit.

---

## Sample Output 📋

```
Do you want to Know your Generation category? (y/n): y
Enter the year you were born: 1990
The Millennials.

Do you want to Know your Generation category? (y/n): n
Good Bye! See you.
```

---

## How to Run ▶️
1. Ensure you have Python installed.
2. Import or define the `common_functions` module with required utility functions (`typing`, `hold_screen`, `clear_screen`, `get_input`).
3. Save the code as `generation_finder.py`.
4. Run the script:
   ```bash
   python generation_finder.py
   ```

---

## Requirements 📦
- Python 3
- `common_functions` module with:
  - **`typing(message: str)`**: Prints a string with typing animation.
  - **`hold_screen()`**: Pauses until the user presses a key.
  - **`clear_screen()`**: Clears the console screen.
  - **`get_input(prompt: str, is_int=False)`**: Gets user input, optionally validating it as an integer.

---

## Customization Ideas ✨
- Add historical trivia or facts about each generation.
- Include an option to enter multiple birth years at once for group categorization.
- Display a graph or visual representation of generations.

---

Discover your generational identity and share it with others! 🎉