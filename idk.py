def is_valid_password(password):
    if len(password) < 8:
        print("Password to short X")
    if not any(char.isdigit for char in password):
        ("Password should contain a number")
    else:
        print("password accepted")
user_password = "secure password"
is_valid_password = user_password

