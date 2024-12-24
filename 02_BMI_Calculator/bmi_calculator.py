from common_functions import typing, hold_screen, clear_screen, get_input

def calculate_bmi(weight, height):
    """Calculate BMI given weight and height."""
    return weight / (height ** 2)

def determine_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight 🧑‍⚖️"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight 🏃"
    elif 25 <= bmi < 29.9:
        return "Overweight 🍔"
    else:
        return "Obese 🚨"

def bmi_calculator():
    '''This program will calculate the Body Mass Index (BMI) for users '''
    clear_screen()
    typing("Welcome to the BMI Calculator! 🎉\n")
    name = get_input("Enter your Name: ")
    height = get_input("Please Share your weight (in kg): ", is_float=True)
    weight = get_input("Please Share your height (in meters): ", is_float=True)

    # BMI Calculation
    bmi = calculate_bmi(height, weight)
    typing(f'\n{name}, your BMI is: {round(bmi, 2)}\n')

    # Category determination
    category = determine_bmi_category(bmi)
    typing(f"Category: {category}\n")
    hold_screen()

def main():
    """Main function to run the BMI calculator."""
    while True:
        clear_screen()
        calculate = get_input("Do you want to calculate your BMI? (yes/no): ").lower()
        
        if calculate == 'yes':
            hold_screen()
            bmi_calculator()
        else:
            typing("Thank you for your time! 😊\n")
            break

# Run the main function
if __name__ == "__main__":
    main()
