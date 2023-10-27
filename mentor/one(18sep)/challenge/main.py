# q -1
# n = int(input())
# for i in range(1,n+1):
#     if i%6==0 or i%14==0:
#         if i%6==0 and i%14==0:
#             continue
#         else:
#             print(i)

# q2
# s = input()
# rev = ''
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# if rev==s:
#     print('Pallindrome')
# else:
    # print('not pallindrome)

# q3
# n = int(input())
# while n!=0:
#     x = n%10
#     if x%2==0:
#         print(x)
#     n = n//10

# q4
# n = int(input())
# find = True
# c=0
# for i in range(1,n+1):
    
#     if n%i==0:
#         c+=1
#     if c>5:
#         find = False
#         print('too many factors')
#         break
        
# if find == True:
#     for i in range(1,n+1):
        
#         if n%i==0:
            
#             print(i)
#     find=False
    