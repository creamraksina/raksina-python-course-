def is_strong_password(password):
    """Checks if password meets strength requirements"""
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    
    if not has_letter:
        return False, "Password must contain at least one letter"
    if not has_number:
        return False, "Password must contain at least one number"
    
    return True, "Password is strong!"

print("Password Validator:")
passwords = ["abc123", "password", "mypass123", "str0ng!", "weak"]
for pwd in passwords:
    is_strong, message = is_strong_password(pwd)
    status = "✓" if is_strong else "✗"
    print(f"{status} '{pwd}': {message}")
print()
