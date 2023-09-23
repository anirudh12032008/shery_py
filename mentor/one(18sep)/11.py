# Question - Take 3 int inputs from user and check and 
# print the result. All are equal any of two are equal
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("At least two numbers are equal.")
else:
    print("None of the numbers are equal to each other.")