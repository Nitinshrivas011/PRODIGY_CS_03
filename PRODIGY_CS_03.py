import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate strength score
    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback based on strength
    if strength_score == 5:
        return "Strong", "Your password is strong. Well done!"
    elif strength_score == 4:
        return "Moderate", "Your password is good but can be improved by adding special characters or numbers."
    elif strength_score == 3:
        return "Weak", "Your password is weak. Consider adding more characters, including uppercase letters, numbers, and special symbols."
    else:
        return "Very Weak", "Your password is too weak. Ensure it has at least 8 characters with uppercase, lowercase, numbers, and special symbols."

if __name__ == "__main__":
    print("Password Strength Checker")
    
    # Get user input for password
    password = input("Enter your password: ")

    # Check password strength
    strength, feedback = check_password_strength(password)
    
    # Display results
    print(f"Password Strength: {strength}")
    print(f"Feedback: {feedback}")
