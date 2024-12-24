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
        