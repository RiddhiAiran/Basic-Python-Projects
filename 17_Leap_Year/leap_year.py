from common_functions import typing, hold_screen, clear_screen, get_input

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0 :
                typing(f"{year} is a Leap Year.\n")
            else:
                typing(f"{year} is not a Leap Year.\n")
        else:
            typing(f"{year} is a Leap Year.\n")
    else:
        typing(f"{year} is not a Leap Year.\n")

def main():
    """Main Function to Run the Game"""
    while True:
        clear_screen()
        status = get_input("Want to check for Leap Year ? (y/n) : ").lower()
        if status == 'y':
            hold_screen()
            clear_screen()
            is_leap_year(get_input("Enter the Year : ", is_int=True))
            hold_screen()
        else:
            typing("Goodbye! 👋 See you next time.\n")
            break

if __name__ == '__main__':
    main()