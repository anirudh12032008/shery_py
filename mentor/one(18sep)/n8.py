# Question - Write a program t0 check wheather the number accepted from user is divisible by 2 and 3 both.
n = int(input("Enter a num: "))
if n%2 == 0 and n%3 == 0 :
    print(f"{n} is divisible by both 2 and 3")
else:
    print(f"{n} is not divisible by both 2 and 3")