from common_functions import typing, hold_screen, clear_screen, get_input

def height_checker(height):
    return height >= 120
    
def fees_with_age(age):
    """Determine the ticket cost based on the age."""
    if 0 < age < 12:
        return 5  # Child ticket cost
    elif 12 <= age < 18:
        return 7  # Teen ticket cost
    elif 18 <= age <= 35:
        return 12  # Adult ticket cost
    else:
        typing("Everything is going to be ok. Have a Free Ride on us! Enjoy\n")
        return 0  # Free ride for others

def roller_coster_ride():
    """Calculate and display permission and fees for the roller coaster ride."""
    clear_screen()
    typing("🎡 Welcome to The Roller Coaster! 🎢\n")
    
    # Get user details
    name = get_input("Enter your Name: ").title()
    height = get_input("Please enter your Height (in cms): ", is_float=True)
    
    if height_checker(height):
        typing("You can ride the roller coaster!\n")

        # Get age and calculate base ticket cost
        age = get_input("What's your Age: ", is_float=True)
        cost = fees_with_age(age)
        
        # Check if the user wants a photo
        photos = get_input("Do you want to take a photo at the photo booth? (Y or N): ").lower()
        if photos == 'y':
            cost += 3  # Add photo cost
        
        typing(f"{name}, Your Final Bill is: ${cost}\n")
    else:
        typing(f"Sorry, {name}, you have to grow taller. You can't ride the roller coaster!\n")
    
    hold_screen()


def main():
    """Main function to run the Roller Coster Ride."""
    while True:
        clear_screen()
        ride = get_input("Do you want to go on the roller coaster ride? (Y or N): ").lower()
        if ride == 'y':
            roller_coster_ride()
        else:
            typing("Thank you for coming! 🎉\n")
            break

# Run the main function
if __name__ == "__main__":
    main()
