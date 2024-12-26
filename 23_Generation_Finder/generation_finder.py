
from common_functions import typing, hold_screen, clear_screen, get_input


def generation():
    clear_screen()
    year = get_input("Enter the year you were born : ",is_int=True)
    if 1901 <= year <= 1924:
        typing("The Greatest Generation\n")
    elif 1925 <= year <= 1945:
        typing("The Silent Generation\n")
    elif 1946 <= year <= 1964:
        typing("The Baby Boomer Generation\n")
    elif 1965 <= year <= 1979:
        typing("Gene-X\n")
    elif 1980 <= year <= 1994:
        typing("The Millennials.\n")
    elif 1995 <= year <= 2009:
        typing("The Gen-Z.\n")
    elif 2010 <= year <= 2025:
        typing("The Gen-Alpha\n")
    else:
        typing("Enter Valid Input.\n")
    hold_screen()

def main():
    while True:
        clear_screen()
        play = get_input("Do you want to Know your Generation category? (y/n) : ").lower()
        if play == 'y':
            hold_screen()
            generation()
        else:
            typing("Good Bye! See you.\n")
            break

if __name__=="__main__":
    main()