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
    print()

def band_name_generator():
    """Generate a band name based on user inputs."""
    clear_screen()
    typing("🎸 Welcome to the Band Name Generator! 🎶\n")
    
    # Get user inputs
    city = input("🏙️  What's the name of the city you grew up in? ").strip()
    pet = input("\n🐾 What's your pet's name? ").strip()
    
    # Display the result
    typing(f"\n✨ Your Band Name Could Be: The {city.title()} {pet.title()} ✨\n")

if __name__ == "__main__":
    band_name_generator()