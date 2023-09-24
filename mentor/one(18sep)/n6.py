# Question - Find maximum number out of given three numbers.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1>n2 and n1>n3:
    print(f"{n1} is the greatest number")
elif n2>n1 and n2>n3:
    print(f"{n2} is the greatest number")
elif n3>n1 and n3>n2:
    print(f"{n3} is the greatest number")
else:
    print("All numbers are equal")