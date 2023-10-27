# 16) Accept an integer and Print hello world n times
# n = int(input("Enter the num: "))
# for i in range(n):
    # print("Hello World")
    
    
# 17) Print natural number up to n. 
# for i in range(1,n+1):
    # print(i)
    
    
    
# 18) Reverse for loop. Print n to 1.
# for i in range(n,0,-1):
    # print(i)
    
    
# 19) Take a number as input and print its table
#        5 * 1 = 5
#        5 * 2 = 10 ... up to 10 terms
# for i in range(1,11):
    # print(f'{n} x {i} = {n*i}')
    
    
    
# 20) Sum up to n terms.
# sum = 0
# for i in range(1,n+1):
    # sum += i
# print(sum)


# 21) Factorial of a number
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(factorial)


# 22) Print the sum of all even & odd numbers in a range seperately.
# # start = int(input("Enter starting of range: "))
# # end = int(input("Enter ending of range: "))
# sumOdd = 0
# sumEven = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         sumEven += i
#     else:
#         sumOdd += i
# print(f"Sum of all even numbers in the range {sumEven}")
# print(f"Sum of all odd numbers in the range {sumOdd}")




# 23) Print all the numbers which are either divisible by 3 or 5 in a range
# for i in range(n)
    # if i%3==0 or i%5==0:
        # print(i)

# 24) Print all the factors of a number.
# for i in range(1,(n//2)+1):
#     if n%i == 0:
#         print(i," ",end="")
# print(n)


# 25) Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43

# sum = 0
# for i in range(1,(n//2)+1):
#     if n%i == 0:
#         sum += i
# print(f"Sum of all Factors of {n} is {sum}")


# 26)  Accept a number and check if it a perfect number or not.
#       A number whose sum of factors(excluding number itself)  = Number 
#       Ex -  6 = 1, 2, 3 = 6
# sum = 0
# for i in range(1,(n//2)+1):
#     if n%i == 0:
#         sum += i
# if sum == n :
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")

    
# 27) Seprate each digit of a number and print it on the new line
# n = input("Enter a num: ")
# x=0
# new =0
# while n != 0:
#     x= n%10
#     n = n//10
#     print(x)
    

# 28) Check if the number is Prime or not.
# # using while loop
# notPrime = True
# i=1
# while notPrime:
#     if n>i+1:  
#         i+=1
#         if n%i ==0 :
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
#         break
# using for loop
# for i in range(2,(n//2)+1):
#     if n%i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")
        

# 29) Accept a number and print its reverse

# x=0
# new =0
# while n != 0:
#     x= n%10
#     n = n//10
#     new = new *10 + x
# print(new)


# 30) Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
#        Ex - 12321 - Rerverse - 12321

# x=0
# new =0
# num = n
# while n != 0:

#     x= n%10
#     n = n//10
#     new = new *10 + x
# if new==num:
#     print("Yes it is a Palindromic Number")
# else:
#     print("No it is not a plaindromic number")

# 31) Tell all the prime numbers in a given range
n=10
t=0
for s in range(2,n+1):
    
    

    c = 0
    for i in range(2,(s//2)+1):
        if s%i == 0:
            c +=1
            break
    if c==0:
        t+=s
        
        print(s,"Prime")
print(t)
# import random
# att = 5
# win = False
# x = random.randint(0,101)
# while not win:
#     n = int(input("Enter the num (1-100):\n"))
    
#     att-=1
#     if att==0:
#         print("Sorry You ran out of attemps")
#         break
#     if n==x:
#         print(f"Congo, You Won in {att} attemps")
#         break
#     elif n>x:
#         print(f"Too big please try something smaller | {att} attemps left ")
#     else:
#         print(f"Too small please try something bigger | {att} attemps left ")
