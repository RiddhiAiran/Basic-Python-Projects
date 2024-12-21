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
    
    typing("Enter your Name: ")
    name = input().title()
    typing(f"\n{name}, Please Share your weight (in kg): ")
    weight = float(input())
    typing("\nPlease Share your height (in meters): ")
    height = float(input())

    # BMI Calculation
    BMI = weight / (height**2)
    typing(f'\nYour BMI as per the details would be: {round(BMI, 2)}\n')

    # Category determination
    if BMI < 18.5:
        typing("Category: Underweight 🧑‍⚖️\n")
    elif 18.5 <= BMI < 24.9:
        typing("Category: Normal Weight 🏃\n")
    elif 25 <= BMI < 29.9:
        typing("Category: Overweight 🍔\n")
    else:
        typing("Category: Obese 🚨\n")

    hold_screen("\nPress Enter to continue...")

while True:
    clear_screen()
    typing("Do you want to calculate your BMI? (yes/no): ")
    calculate = input().lower()
    if calculate == 'yes':
        hold_screen("\nPress Enter to continue...")
        BMI_Calculator()
    else:
        typing("Thank you for your time! 😊\n")
        break
