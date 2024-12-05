import re
def validate_password(password):
    """Validates a password based on specified conditions and assesses its strength."""
    conditions = [
        len(password) == 8,
        password[0].isupper(),
        password[-1].islower(),
        any(char in "!@#$%^&*()_+-=[]{}|;:'\"\\|,.<>/?" for char in password),
        not re.search(r"\s", password),
    ]
    if all(conditions):
        print("Password is valid.")
        has_digit = any(char.isdigit() for char in password)
        if has_digit:
            print("Password is strong.")
        else:
            print("Password could be stronger. Consider adding a digit.")
    else:
        print("Password is invalid. Please ensure it meets the following criteria:")
        for condition in conditions:
            if not condition:
                print(f"  - {condition.replace('not ', '')}")
if __name__ == "__main__":
    password = input("Enter a password: ")
    validate_password(password)
