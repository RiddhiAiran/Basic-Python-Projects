from common_functions import typing, hold_screen, clear_screen, get_input

def band_name_generator():
    """Generate a band name based on user inputs."""
    clear_screen()
    typing("🎸 Welcome to the Band Name Generator! 🎶\n")
    
    # Get user inputs with the typing effect
    city = get_input("\n🏙️  What's the name of the city you grew up in? ")
    pet = get_input("\n🐾 What's your pet's name? ")
    
    # Generate and display the result
    typing(f"\n✨ Your Band Name Could Be: The {city} {pet} ✨\n")

if __name__ == "__main__":
    band_name_generator()
    
