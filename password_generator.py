import random

BOLD = "\033[1m"
RESET = "\033[0m"

def generate_password(length, include_upper, include_lower, include_numbers, include_symbols):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "#!$@"

    allowed_characters = ""

    allowed_characters += upper_case if include_upper == "y" else ""
    allowed_characters += lower_case if include_lower == "y" else ""
    allowed_characters += numbers if include_numbers == "y" else ""
    allowed_characters += symbols if include_symbols == "y" else ""

    if length < 1:
        print("\nERROR: Password length must be bigger than 0.")

    if len(allowed_characters) == 0:
        print("\nERROR: You must choose atlesat one set of characters.")

    password = "".join(random.choice(allowed_characters) for _ in range(length))

    return password
        

length = int(input("Enter the length of your password: "))
upper_case = input("Do you want to include uppercase characters (Y/n)? ").lower()
lower_case = input("Do you want to include lowercase characters (Y/n)? ").lower()
numbers = input("Do you want to include numbers (Y/n)? ").lower()
symbols = input("Do you want to include symbols (Y/n)? ").lower()

password = generate_password(length, upper_case, lower_case, numbers, symbols)

print("\n  Generated password")
print("----------------------")
print(f"{BOLD}{password}{RESET}")