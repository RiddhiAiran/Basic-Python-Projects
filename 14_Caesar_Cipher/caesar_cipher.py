from .logo import logo
from common_functions import typing, hold_screen, clear_screen, get_input

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar():
    """Encoder Decoder Main Program"""
    clear_screen()
    print(logo)
    direction = get_input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction not in ['encode', 'decode']:
        typing("Invalid option. Please choose 'encode' or 'decode'.\n")
    else:
        text = get_input("Type your message: ").lower()
        shift_amount = get_input("Type the shift number: ",is_int=True)
    output_text = ''
    if direction == 'decode':
        shift_amount *= -1
    for letter in text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    typing(f"Here is the {direction} result : {output_text}\n")

# Main program
def main():
    """Main Function to Run the Program"""
    while True:
        clear_screen()
        status = get_input("Type 'yes' if you want to encode/decode your message. Otherwise type 'no' :").lower()
        if status == "yes":
            hold_screen()
            caesar()
            hold_screen()
        else:
            typing("Good Bye\n")
            break
        
if __name__ == '__main__':
    main()
        