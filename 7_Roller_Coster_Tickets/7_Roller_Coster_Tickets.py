import os 
import time

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

def roller_coster_ride():
    """This program will check and give the permision and fees of the roller coster ride"""
    cost = 0
    clear_screen()
    typing("🎡 Welcome to The Roller Coster! 🎢\n")
    typing("Enter your Name : ")
    name = input().title()
    typing(f"{name}, Please enter your Hieght (in cms) : ")
    height = float(input())
    if height >= 120:
        typing("You can ride the roller coster!\n")
        typing("What's your Age : ")
        age = int(input())
        if 0 < age < 12:
            cost += 5
        elif 12 <= age < 18:
            cost += 7
        elif 18 <= age <= 35:
            cost += 12
        else:
            typing("Everything is going to be ok. Have a Free Ride on us! Enjoy\n")
        
        typing("Do you want to take photo at photo booth? Y or N : ")
        photos = input().lower()
        if photos == 'y':
            cost += 3
        
        typing(f"{name}, Your Final Bill is : ${cost}\n")
        hold_screen()
    else:
        typing(f"Sorry, {name} You Have to grow taller, You can't ride the roller coster!\n")
        hold_screen()



while True:
    clear_screen()
    typing("Do you want to Go to the roller coster ride?(y or n) : ")
    ride = input().strip().lower()
    if ride == 'y':
        hold_screen()
        roller_coster_ride()
    else:
        typing("Thank you for Coming ! \n")
        break