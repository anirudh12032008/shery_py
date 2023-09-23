# Question - Accept two numbers from user and swap their values
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# Method 1 
c = a
a = b
b = c
# Method 2 
a,b = b,a
# Method 3
a = a + b
b = a - b
a = a - b
print(f"After swapping : num1 = {a}, num2 = {b}")
