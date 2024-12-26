import random
from common_functions import typing, hold_screen, clear_screen, get_input
import time 


def total_words():
    """Returns the total words in a book"""
    clear_screen()
    typing("Welcome to the Words in the Book Checker!\n")
    pages = get_input("Enter the Total Number of Pages in The Book : ", is_int=True)
    words_per_page = get_input("Number of Words Per Page : ", is_int=True)
    total = pages * words_per_page
    typing(f"The Book Will have {total} Words in {pages} Pages.\n")


if __name__ == "__main__":
    total_words()