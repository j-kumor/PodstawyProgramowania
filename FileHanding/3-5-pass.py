###
# Checks the correctness of username and password
#
import re

username = input("Enter username: ")
password = input("Enter password: ")

username_pattern = '^[a-z]{6,}$'
password_pattern = '^[a-zA-Z0-9_]{8,}$'

username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_match and password_match:
    print("Username and password are valid.")
else:
    if not username_match:
        print("Invalid username")
    if not password_match:
        print("Invalid password")
