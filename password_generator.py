import random
import string

def generate_password(length,):
    c = string.ascii_letters + string.digits
    password = ''.join(random.choice(c) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired length of the password: "))
    
    if length < 1:
        print("Password length should be at least 1.")
    else:
        print(f"Generated password: {generate_password(length)}")
except ValueError:
    print("Please enter a valid number.")
