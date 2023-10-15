s = input("Enter the string: ")
# 31) Print string in reverse,its length,in uppercase,lowercase and copy into another string
# print(s[::-1])
# print(len(s))
# print(s.lower())
# print(s.upper())
# str2 = s[::]
# print(str2)

# 32) Arrange string characters such that lowercase letters should come first
# strlow=""
# strelse=""
# for i in s:
#     if i.islower():
#         strlow += i
#     else:
#         strelse += i
# print (strlow+strelse)
        

# 33) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
#     Total counts of chars, digits, and symbols
#     Chars = 8
#     Digits = 3
#     Symbol = 4
# char = 0
# dig = 0
# sym = 0
# for i in s:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         dig += 1
#     else:
#         sym += 1
# print("Total counts of chars, digits, and symbols")
# print("Chars =", char)
# print("Digits =", dig)
# print("Symbol =", sym)

# # 34) Compare two strings without using inbuilt functionsx
# a = 'llohe'
# if len(a)!=len(s):
#     print("Not smilar")
# else:     
#     similar = False
#     for i in s:
#         if i in a:
#             similar = True
#             continue
    #     else:
    #         similar = False
    #         break
    # if similar: 
    #     for i in a:
    #         if i in s:
    #             similar = True
    #             continue
    #         else:
    #             similar = False
    #             break
    # if similar:
    #     print("Similar")
    # else:
    #     print("Not similar")
        

# 35) Count Vowels from given string
# vow = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         vow += 1
# print(vow)

# 36) Reverse a string
# print(s[::-1])
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev += s[i]
# print(rev)
# 37) Check string is Pallindrome or not**
# if s==s[::-1]:
#     print(f"{s} is a Pallindrome")
# else:
#     print(f"{s} is not a Pallindrome")

# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev += s[i]
# if rev==s:print('Pallindrome')





