# cook your dish here
t = int(input())
for i in range(t):
    x,y = input().split()
    if int(x)>=int(y):
        print("great")
        print(int(y))
    else:
        print(((int(y)-int(x))*2)+(int(x)))