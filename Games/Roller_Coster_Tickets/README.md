# Roller Coaster Ride Program 

Welcome to the **Roller Coaster Ride Program**! This Python program checks eligibility, calculates ride fees based on age, and optionally adds a photo booth charge—all with a fun typing effect and interactive user experience.

---

## Program Demo

Below is a quick demo of the Roller Coaster Ride program:
![project7](https://github.com/user-attachments/assets/437577cc-a8d8-43df-9c1b-ae43b290a173)

---

## 🚀 Features

- **Typing Effect:** Displays text character by character for an engaging experience.
- **Clear Screen Function:** Keeps the terminal clean and focused.
- **Ride Eligibility:** Checks height requirements to determine if a user can ride.
- **Age-Based Pricing:**
   - Kids under 12: $5
   - Teenagers (12-17): $7
   - Adults (18-35): $12
   - Seniors (36+): Free ride!
- **Photo Booth Option:** Optionally adds $3 to the bill for a ride photo.
- **Repeatable Session:** Allows multiple users to go for rides.
- **Graceful Exit:** Exit the program anytime.

---

## 📚 Concepts Needed

To understand and modify this program, you should be familiar with:

1. **Python Basics:** Variables, Functions, Loops, and Conditionals.
2. **Input/Output:** Taking user input and displaying outputs interactively.
3. **String Manipulation:** Formatting strings for dynamic messaging.
4. **Control Flow:** Managing program execution with loops and conditionals.
5. **Modules:**
   - `os`: For clearing the terminal screen.
   - `time`: To implement the typing effect.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd Games/Roller_Coster_Tickets
   ```

2. **Run the Program:**
   Ensure you have Python installed on your system. Execute the script using:
   ```bash
   python roller_coster_tickets.py
   ```

3. **Follow the Prompts:**
   - Enter your name and height.
   - Input your age to calculate the ride cost.
   - Choose whether you want a photo at the photo booth.
   - View the final bill and enjoy the ride!

---

## Code Explanation

The main logic is implemented in the `roller_coster_ride` function:

1. **`clear_screen()`**: Clears the console for a clean user experience.
2. **`typing(message, delay)`**: Simulates typing text with a delay.
3. **`hold_screen()`**: Pauses the screen until the user presses Enter.
4. **`roller_coster_ride()`**:
   - Prompts for user details: name, height, and age.
   - Checks if the height is sufficient to ride.
   - Calculates the ride cost based on age:
     - Under 12 years: $5
     - 12-17 years: $7
     - 18-35 years: $12
     - Over 35 years: Free ride.
   - Optionally adds $3 for a photo booth picture.
   - Displays the final bill.
5. **Loop for Multiple Rides:** The program keeps running until the user exits.

---

## Example Output

```plaintext
🎡 Welcome to The Roller Coster! 🎢
Enter your Name : Alice
Alice, Please enter your Hieght (in cms) : 130
You can ride the roller coster!
What's your Age : 15
Do you want to take photo at photo booth? Y or N : Y
Alice, Your Final Bill is : $10
Press Enter to continue...

Do you want to Go to the roller coster ride?(y or n) : n
Thank you for Coming !
```

---

## 🚑 Acknowledgements

This program was inspired by amusement park experiences and is designed for learners to practice Python control structures and input handling. It’s a great way to simulate real-world scenarios!

---

Enjoy Coding! 🎡🎢
