import os 
import time
import random 

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

def pypassword():
    """Generate a random secure password based on user input."""
    # Characters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!@#$%^&*()-_'
    numbers = '1234567890'

    while True :
        clear_screen()
        typing("Welcome to the Python Password Generator!\n")
        typing("How Many Letters do you want ? ")
        n_letters = int(input().strip())
        typing("How Many Symbols do you want ? ")
        n_symbols = int(input().strip())
        typing("How Many Numbers do you want ? ")
        n_numbers = int(input().strip())

        if n_letters < 0 or n_symbols < 0 or n_numbers < 0:
            typing("Please enter Positive Numbers for all inputs.\n")
            hold_screen()
        else:
            break
    password = (random.choices(letters, k=n_letters)
                + random.choices(symbols, k=n_symbols)
                + random.choices(numbers, k=n_numbers))
    
    random.shuffle(password)
    generated_password = ''.join(password)
    typing(f"\nYour Secure Password is: {generated_password}\n")

pypassword()
