from common_functions import typing, hold_screen, clear_screen, get_input

def is_prime():
    clear_screen()
    typing("Welcome to the prime number checker !\n")
    num = get_input("Enter your number : ", is_int=True)
    for i in range(2,num):
        if num%i == 0:
            return False
    else:
        return True

def main():
    while True:
        clear_screen()
        check = get_input("Do you want to check wheather a number is prime or not ? (y/n) :").lower()
        if check == 'y':
            hold_screen()
            prime = is_prime()
            if prime:
                typing("It's a Prime Number.\n")
            else:
                typing("It's not a Prime Number.\n")
            hold_screen()
        else:
            typing("Good Bye! See You.\n")
            break
            
if __name__ == "__main__":
    main()
    