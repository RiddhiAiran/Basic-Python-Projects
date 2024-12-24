from common_functions import typing, hold_screen, clear_screen, get_input


def calculate_love_score(name1, name2):
    """Main Logic of the program"""
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Define the letters for TRUE and LOVE
    true_letters = 'true'
    love_letters = 'love'
    
    # Calculate the score for TRUE
    true_score = sum(combined_names.count(letter) for letter in true_letters)
    
    # Calculate the score for LOVE
    love_score = sum(combined_names.count(letter) for letter in love_letters)
    
    # Combine scores into a two-digit number
    love_score_combined = str(true_score) + str(love_score)
    print(int(love_score_combined))

# Main program
def main():
    """Main Function to Run the Program"""
    while True:
        clear_screen()
        status = get_input("Do you want to calculate your love? (y/n) : ").lower()
        if status == "y":
            calculate_love_score(get_input("Enter Your Name : "), get_input("Enter your Partner Name: "))
            hold_screen()
        else:
            typing("Good Bye!\n")
            break
        
if __name__ == '__main__':
    main()