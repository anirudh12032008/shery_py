import random
att = 5
win = False
x = random.randint(1,10)
while not win:
    n = int(input("Enter the num (1-10):\n"))
    att-=1
    if n==x:
        print(f"Congo, You Won in {5-att} attemps")
        break
    if att==0:
        print("Sorry You ran out of attemps the number was", x)
        break
    elif n>x:
        print(f"Too big please try something smaller | {att} attemps left ")
    else:
        print(f"Too small please try something bigger | {att} attemps left ")