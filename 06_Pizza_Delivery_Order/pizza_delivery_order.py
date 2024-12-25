from common_functions import typing, hold_screen, clear_screen, get_input

def pizza_bill(size, pepperoni, extra_cheese):
    """Calculate the total pizza bill based on size, pepperoni, and cheese options."""
    # Base prices
    size_prices = {'S': 15, 'M': 20, 'L': 25}
    pepperoni_prices = {'S': 2, 'M': 3, 'L': 3}

    bill = size_prices[size]
    if pepperoni == 'Y':
        bill += pepperoni_prices[size]
    if extra_cheese == 'Y':
        bill += 1  # Extra cheese cost
    return bill

def pizza_order():
    """Handle the pizza ordering process."""
    clear_screen()
    typing("🍕🍕 Welcome to the Pizza Order Machine!🍕 \n")
    name = get_input("Enter your Name: ")
    size = get_input("🫓 What Size Pizza do you want? S, M or L?: ").upper()
    pepperoni = input("🥫 Do you want Pepperoni on your pizza? Y or N: ").upper()
    extra_cheese = input("🧀 Do you want extra Cheese? Y or N: ").upper()
    bill = pizza_bill(size,pepperoni,extra_cheese)
    hold_screen()
    clear_screen()
    # Provide feedback
    typing(f"\nThank you, {name}! Here's your order summary:\n")
    typing(f"   - Pizza Size: {size}\n")
    typing(f"   - Pepperoni: {'Yes' if pepperoni == 'Y' else 'No'}\n")
    typing(f"   - Extra Cheese: {'Yes' if extra_cheese == 'Y' else 'No'}\n")
    typing(f"\n💵 Your Final Bill is: ${bill}\n")
    typing("Enjoy your pizza! 🍕🍕\n")
    hold_screen()

def main():
    """Main Function to run the pizza order. """
    while True:
        clear_screen()
        order = get_input("Do you want to Order a Pizza 🍕 ? (Y or N) : ").upper()
        if order == 'Y':
            hold_screen()
            pizza_order()
        else:
            typing("Goodbye! 👋\n")
            break

if __name__ == '__main__':
    main()