# Question - The given number is positive or negative or zero
n = int(input("Enter a Number:"))
if n > 0:
    print(f"{n} is  a Positive Number")
elif n < 0:
    print(f"{n} is a Negative Number")
elif n == 0:
    print(f"{n} is equal to 0")
else:
    print("Inavlid input. Please write a integer")
