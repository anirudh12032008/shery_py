# Question - The given character is an uppercase letter or lowercase letter or a digit or a special character.
# Question - The given character is an uppercase letter or lowercase letter or a digit or a special character.
char = input("Enter a character: ")

if 'A' <= char <= 'Z':
    print(f"'{char}' is an Uppercase Letter")

elif 'a' <= char <= 'z':
    print(f"'{char}' is a Lowercase Letter")

elif '0' <= char <= '9':
    print(f"'{char}' is a Digit")

else:
    print(f"'{char}' is a Special Character")
