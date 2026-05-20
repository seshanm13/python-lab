def check_password_strength(password):
    has_digit = False
    has_upper = False
    has_lower = False
    is_long_enough = len(password) >= 8
    
    for char in password:
        if char.isdigit(): has_digit = True
        if char.isupper(): has_upper = True
        if char.islower(): has_lower = True

    if has_digit and has_upper and has_lower and is_long_enough:
        return "Strong Password"
    else:
        # Building simple feedback context
        return "Weak Password (Ensure it has minimum 8 chars, uppercase, lowercase, and digits)"

pwd = input("Enter password to test: ")
print("Strength Result:", check_password_strength(pwd))