import random 
from common_functions import typing, hold_screen, clear_screen, get_input

def pypassword():
    """Generate a random secure password based on user input."""
    # Characters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!@#$%^&*()-_'
    numbers = '1234567890'

    while True :
        clear_screen()
        typing("Welcome to the Python Password Generator!\n")
        n_letters = get_input("How Many Letters do you want ? ",is_int=True)
        n_symbols = get_input("How Many Symbols do you want ? ",is_int=True)
        n_numbers = get_input("How Many Numbers do you want ? ",is_int=True)
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
    hold_screen()

#Main Loop
def main():
    """Main Function to Run the Generator"""
    while True:
        clear_screen()
        start = get_input("Want to Generate a Strong Password? (yes/no) :").lower()
        if start == 'yes':
            hold_screen()
            pypassword()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break

if __name__ == '__main__':
    main()