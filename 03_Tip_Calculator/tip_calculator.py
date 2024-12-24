from common_functions import typing, hold_screen, clear_screen, get_input

def tip_calculator():
    '''Generate Total Bill Amount Each Person will Pay Including Tip'''
    clear_screen()
    typing("🧾 Welcome to the Tip Calculator! 😇\n")

    bill = get_input("\n💵 What was the Total Bill? $", is_float=True)
    tip = get_input("\n 📝 How much tip would you like to give? 10, 12, or 15? : ", is_float=True)
    spliting = get_input("\n 🧑‍🧑‍🧒‍🧒 How many people to split the bill? (at least 1) : ", is_float=True)
    total_bill = bill + (bill*(tip/100))
    each_share = total_bill/spliting
    print("-"*70)
    typing(f"\nYour Total Bill with Tip Would Be: ${round(total_bill, 2)}\n")
    typing(f"\nEach Person Should Pay: ${round(each_share, 2)}\n")
    print("\n")
    hold_screen()

def main():
    """Main function to run the Tip calculator."""
    while True:
        clear_screen()
        calculate = get_input("Do you want to use Tip Calculator? (yes/no): ").lower()
        if calculate == 'yes':
            hold_screen()
            tip_calculator()
        else:
            typing("Thank you for your time! 😊\n")
            break

# Run the main function
if __name__ == "__main__":
    main()
