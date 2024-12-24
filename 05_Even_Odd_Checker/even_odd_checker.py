from common_functions import typing, hold_screen, clear_screen, get_input

def even_odd():
    """Check if Number is Even or Odd"""
    clear_screen()
    typing("Welcome to the Even and Odd Number Checker !\n")
    num = get_input("Enter your Number : ",is_int=True)
    if num % 2 == 0:
        typing(f"{num} is an Even Number \n")
    else:
        typing(f"{num} is an Odd Number \n")
    hold_screen()
    
def main():
    """Main function to run the Checker."""
    while True:
        clear_screen()
        check = get_input("Do you want to Check a Number is even or Odd ? (y/n) : ").lower()
        if check == 'y':
            hold_screen()
            even_odd()
        else:
            typing('Thank you for Coming!\n')
            break

# Run the main function
if __name__ == "__main__":
    main()
    