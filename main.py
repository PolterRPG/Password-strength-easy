def check_password_strength(password):
    score = 0

    if len(password) >= 10:
        score += 1

    for char in password:
        if char.isdigit():
            score += 1
            break

    special_characters = "!@#$%^&*"
    for char in password:
        if char in special_characters:
            score += 1
            break

    if score > 4:
        return "Strong password "
    elif score == 3:
        return "Medium password "
    else:
        return "Weak password "


user_password = input("Enter a password: ")
result = check_password_strength(user_password)
print(result)
