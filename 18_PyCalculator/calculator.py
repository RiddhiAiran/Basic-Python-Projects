from .logo import logo
from common_functions import typing, hold_screen, clear_screen, get_input

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
    n1 = get_input("Enter Your First Number : ", is_float=True)
    while True: 
        for ope in operations:
            print(ope)
        operator = get_input("Pick an operation: ")
        n2 = get_input("Enter Your Next Number : ", is_float=True)
        result = operations[operator](n1,n2)
        typing(f" {n1} {operator} {n2} = {result}\n")
        status = get_input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if status == 'y':
            n1 = result
            continue
        else:
            calc()

if __name__ == '__main__':
    calc()
