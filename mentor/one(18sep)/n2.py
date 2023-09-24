# Question - The given number is of one digited or two digited or three digited or more than three digited.

n = int(input("Enter a number:"))

if -9 <= n <= 9:
    digit_type = "One Digit"
elif -99 <= n <= 99:
    digit_type = "Two Digit"
elif -999 <= n <= 999:
    digit_type = "Three Digit"
else:
    digit_type = "More than Three Digit"

print(f"{n} is {digit_type}.")
