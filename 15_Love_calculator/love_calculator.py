def calculate_love_score(name1, name2):
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

calculate_love_score("Angela Yu","Jack Bauer")