import os 
import time

from logo import logo

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

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    '-' : subtract ,
    '*' : multiply,
    '/' : divide
}


def calc():
    clear_screen()
    print(logo)
    typing("Welcome To Python Calculator ! \n")
    typing("Enter Your First Number : ")
    n1 = float(input())
    while True: 
        for ope in operations:
            print(ope)
        typing("Pick an operation: ")
        operator = input()
        typing("Enter Your Next Number : ")
        n2 = float(input())
        result = operations[operator](n1,n2)
        typing(f" {n1} {operator} {n2} = {result}\n")
        typing(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        status = input().strip().lower()
        if status == 'y':
            n1 = result
            continue
        else:
            calc()
            break

calc()
