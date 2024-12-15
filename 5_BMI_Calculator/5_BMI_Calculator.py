import time
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)


def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

def BMI_Calculator():
    '''This program will calculate the Body Mass Index (BMI) for users '''
    clear_screen()
    typing("Welcome to the BMI Calculator! 🎉\n")
    
    typing("\nEnter your Name: ")
    name = input().title()
    
    # Input for weight with validation
    while True:
        try:
            typing(f"\n{name}, Please Share your weight (in kg): ")
            weight = float(input())
            if weight <= 0:
                raise ValueError("\nWeight must be greater than 0.")
            break
        except ValueError as e:
            typing(str(e))

    # Input for height with validation
    while True:
        try:
            typing("\nPlease Share your height (in meters): ")
            height = float(input())
            if height <= 0:
                raise ValueError("\nHeight must be greater than 0.")
            break
        except ValueError as e:
            typing(str(e))
    
    # BMI Calculation
    BMI = weight / (height**2)
    typing(f'\nYour BMI as per the details would be: {round(BMI, 2)}\n')

    # Category determination
    if BMI < 18.5:
        typing("\nCategory: Underweight 🧑‍⚖️\n")
    elif 18.5 <= BMI < 24.9:
        typing("\nCategory: Normal Weight 🏃\n")
    elif 25 <= BMI < 29.9:
        typing("\nCategory: Overweight 🍔\n")
    else:
        typing("\nCategory: Obese 🚨\n")

    hold_screen("\nPress Enter to continue...")

while True:
    clear_screen()
    typing("\nDo you want to calculate your BMI? (yes/no): ")
    calculate = input().lower()
    if calculate == 'yes':
        BMI_Calculator()

        # Ask for recalculation 
        typing("\nDo you want to recalculate (yes) or exit (no)? ")
        status = input().lower()
        if status != 'yes':
            typing("Thank you for coming! Goodbye 👋\n")
            break
    else:
        typing("Thank you for your time! 😊")
        break

